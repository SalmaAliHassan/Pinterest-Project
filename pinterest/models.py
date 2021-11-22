from django.db import models
from django.contrib.auth.models import AbstractUser


LIKES_CHOICES = (
    {'H', 'Heart'},
    {'L', 'Like'},
    {'J', 'Joyful'},
    {'H', 'Haha'},
)

GENDER_CHOICES = (
    {'F', 'Female'},
    {'M', 'Male'}
)

class User(AbstractUser):
    # following = models.ForeignKey('self', null=True,related_name='followedBy',on_delete=models.CASCADE)

    gender = models.CharField(choices= GENDER_CHOICES, max_length=50, null=True )
    followers = models.ManyToManyField(
        to='self',
        related_name='followees',
        symmetrical=False
    )

    def __str__(self):
        return self.username
# Create your models here.

class Pin(models.Model):
    title= models.CharField(max_length=50)
    alt_description= models.CharField(max_length=250, null=True, default='')
    pin_picture = models.ImageField(upload_to='photos', null = True, blank = True)
    destination_link = models.URLField(max_length=200, null= True)
    owner= models.ForeignKey('User',related_name='pins',on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Board(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Section(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Note(models.Model):
    title = models.CharField(max_length=50)
    content  = models.TextField(max_length=500)
    content_picture = models.ImageField(upload_to='photos')

    def __str__(self):
        return self.title 


class Notification(models.Model):
    content  = models.TextField(max_length=500)
    creation_date = models.DateField()
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.creation_date


class Comment(models.Model):
    content  = models.TextField(max_length=500)

    def __str__(self):
        return self.content

class Like(models.Model):
    type  = models.CharField(max_length=500, choices= LIKES_CHOICES )

    def __str__(self):
        return self.type

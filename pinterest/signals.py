from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from .models import User

@receiver(post_save, sender=User)
def usercreateHandler(sender,instance,created,**prams):
    if created:
        Token.objects.create(user=instance)

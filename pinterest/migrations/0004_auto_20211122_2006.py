# Generated by Django 3.2.9 on 2021-11-22 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinterest', '0003_pin_pin_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[{'Heart', 'H'}, {'Like', 'L'}, {'Joyful', 'J'}, {'Haha', 'H'}], max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(max_length=500)),
                ('content_picture', models.ImageField(upload_to='photos')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=500)),
                ('creation_date', models.DateField()),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='pin',
            name='destination_link',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[{'F', 'Female'}, {'M', 'Male'}], max_length=50, null=True),
        ),
    ]

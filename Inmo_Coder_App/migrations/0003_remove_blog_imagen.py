# Generated by Django 4.1 on 2022-09-13 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inmo_Coder_App', '0002_blog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='imagen',
        ),
    ]

# Generated by Django 4.1 on 2022-09-12 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inmo_Coder_App', '0002_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avatar',
            old_name='image',
            new_name='imagen',
        ),
    ]

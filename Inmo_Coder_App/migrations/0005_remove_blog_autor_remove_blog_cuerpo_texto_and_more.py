# Generated by Django 4.1 on 2022-09-13 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inmo_Coder_App', '0004_blog_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='cuerpo_texto',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='fecha_creacion',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='sub_titulo',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='titulo',
        ),
    ]

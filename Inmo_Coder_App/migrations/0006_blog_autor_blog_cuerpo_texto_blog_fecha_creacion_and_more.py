# Generated by Django 4.1 on 2022-09-13 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inmo_Coder_App', '0005_remove_blog_autor_remove_blog_cuerpo_texto_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='autor',
            field=models.CharField(default='fede', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='cuerpo_texto',
            field=models.CharField(default='fede', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='fecha_creacion',
            field=models.DateField(default='2022-05-05'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='sub_titulo',
            field=models.CharField(default='fede', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='titulo',
            field=models.CharField(default='fede', max_length=50),
            preserve_default=False,
        ),
    ]
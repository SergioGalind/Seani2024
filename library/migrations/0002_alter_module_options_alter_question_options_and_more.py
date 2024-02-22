# Generated by Django 5.0.2 on 2024-02-22 17:06

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='module',
            options={'verbose_name': 'módulo', 'verbose_name_plural': 'módulos'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'pregunta', 'verbose_name_plural': 'preguntas'},
        ),
        migrations.AlterField(
            model_name='module',
            name='description',
            field=models.CharField(max_length=100, verbose_name='Descripcion del modulo'),
        ),
        migrations.AlterField(
            model_name='module',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Nombre del modulo'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Imagen de la pregunta'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Texto de la pregunta'),
        ),
    ]

# Generated by Django 4.0.5 on 2022-07-27 19:24

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='masdatosusuarios',
            name='Link',
            field=models.URLField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='masdatosusuarios',
            name='descripcion',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
# Generated by Django 4.1.4 on 2022-12-25 20:20

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_yazilarmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yazilarmodel',
            name='icerik',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
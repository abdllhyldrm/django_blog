# Generated by Django 4.1.4 on 2022-12-25 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_iletisimmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='yorummodel',
            old_name='guncellenme_tarihi',
            new_name='duzenlenme_tarihi',
        ),
        migrations.AlterField(
            model_name='yorummodel',
            name='olusturulma_tarihi',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

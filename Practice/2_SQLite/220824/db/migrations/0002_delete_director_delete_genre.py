# Generated by Django 4.0.6 on 2022-08-24 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Director',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
    ]

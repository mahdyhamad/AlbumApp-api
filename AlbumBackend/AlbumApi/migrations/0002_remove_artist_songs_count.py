# Generated by Django 3.0.5 on 2020-04-27 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AlbumApi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='songs_count',
        ),
    ]

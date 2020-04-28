# Generated by Django 3.0.5 on 2020-04-27 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Album Title')),
                ('year_released', models.PositiveIntegerField()),
                ('number_of_songs', models.PositiveIntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Artist Name')),
                ('date_of_birth', models.DateField()),
                ('songs_count', models.PositiveIntegerField(blank=True, null=True, verbose_name='Number of Songs')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Song Title')),
                ('date_created', models.DateField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='AlbumApi.Album')),
                ('artist', models.ManyToManyField(related_name='songs', to='AlbumApi.Artist')),
            ],
        ),
    ]
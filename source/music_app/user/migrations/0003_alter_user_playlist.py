# Generated by Django 3.2.12 on 2022-03-30 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0003_alter_playlist_music'),
        ('user', '0002_alter_user_playlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='playlist',
            field=models.ManyToManyField(blank=True, to='playlist.Playlist'),
        ),
    ]

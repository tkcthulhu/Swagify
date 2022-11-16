# Generated by Django 4.1.3 on 2022-11-15 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_song_artist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='artist',
            new_name='main_artist',
        ),
        migrations.AddField(
            model_name='song',
            name='feat_artist',
            field=models.ManyToManyField(related_name='Featured', to='API.artist'),
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-15 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_tag_playlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='artist',
            field=models.ManyToManyField(to='API.artist'),
        ),
    ]

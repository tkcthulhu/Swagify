# Generated by Django 4.1.3 on 2022-11-18 14:32

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('date_released', models.DateField()),
                ('compilation', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('listeners', models.IntegerField()),
                ('bio', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('user_generated', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('explicit', models.BooleanField()),
                ('length', models.DurationField()),
                ('plays', models.IntegerField()),
                ('feat_artist', models.ManyToManyField(blank=True, related_name='Feat', to='API.artist')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.genre')),
                ('main_artist', models.ManyToManyField(to='API.artist')),
            ],
        ),
        migrations.CreateModel(
            name='PlaylistOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_num', models.SmallIntegerField()),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='API.playlist')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='API.song')),
            ],
        ),
        migrations.AddField(
            model_name='playlist',
            name='songs',
            field=models.ManyToManyField(through='API.PlaylistOrder', to='API.song'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='tags',
            field=models.ManyToManyField(to='API.tag'),
        ),
        migrations.CreateModel(
            name='AlbumOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_num', models.SmallIntegerField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='API.album')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='API.song')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='songs',
            field=models.ManyToManyField(through='API.AlbumOrder', to='API.song'),
        ),
    ]

from django.db import models

# Create your models here.

class Artist(models.Model):

    name = models.CharField(max_length=50)
    listeners = models.IntegerField()
    bio = models.TextField(max_length=500)

    def __str__(self):
        return self.name

class Genre(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Song(models.Model):

    title = models.CharField(max_length=50)
    main_artist = models.ManyToManyField('Artist')
    feat_artist = models.ManyToManyField('Artist', related_name='Feat', blank=True)
    explicit = models.BooleanField()
    length = models.DurationField()
    plays = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} artist: {self.main_artist.first()}'

class Album(models.Model):

    title = models.CharField(max_length=50)
    date_released = models.DateField()
    compilation = models.BooleanField()
    songs = models.ManyToManyField('Song', through='AlbumOrder')

    def __str__(self):
        return self.title

class AlbumOrder(models.Model):

    track_num = models.SmallIntegerField()
    song = models.ForeignKey('Song', on_delete=models.PROTECT)
    album = models.ForeignKey('Album', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.album} track {self.track_num}: {self.song}'

class Tag(models.Model):

    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class PlaylistOrder(models.Model):
    track_num = models.SmallIntegerField()
    song = models.ForeignKey('Song', on_delete=models.PROTECT)
    playlist = models.ForeignKey('Playlist', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.playlist} track {self.track_num}: {self.song}'


class Playlist(models.Model):

    title = models.CharField(max_length=50)
    user_generated = models.BooleanField()
    songs = models.ManyToManyField(Song, through='PlaylistOrder')
    tags = models.ManyToManyField('Tag')
    
    def __str__(self):
        return self.title
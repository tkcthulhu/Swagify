from django.db import models

# Create your models here.

class Artist(models.Model):

    name = models.CharField(max_length=50)
    listers = models.IntegerField()
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
    feat_artist = models.ManyToManyField('Artist', related_name='Feat')
    explicit = models.BooleanField()
    length = models.DurationField()
    plays = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Album(models.Model):

    title = models.CharField(max_length=50)
    date_released = models.DateField()
    compilation = models.BooleanField()
    songs = models.ManyToManyField('Song')

    def __str__(self):
        return self.title

class Tag(models.Model):

    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Playlist(models.Model):

    title = models.CharField(max_length=50)
    user_generated = models.BooleanField()
    songs = models.ManyToManyField('Song')
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title
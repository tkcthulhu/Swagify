from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Artist, Genre, Song, Album, Playlist, Tag



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['name', 'listeners', 'bio']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']

class SongSerializer(serializers.ModelSerializer):

    main_artist = ArtistSerializer()
    feat_artist = ArtistSerializer()
    genre = GenreSerializer()

    class Meta:
        model = Song
        fields = ['title', 'main_artist', 'feat_artist', 'explicit', 'length', 'plays', 'genre']

class SongAlbumViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['title']

class ArtistAlbumViewSerializer(serializers.ModelSerializer):

    Artist = ArtistSerializer()

    class Meta:
        model = Song
        fields = ['Artist']

class AlbumSerializer(serializers.ModelSerializer):

    artist = ArtistAlbumViewSerializer()
    songs = SongAlbumViewSerializer()

    class Meta:
        model = Album
        fields = ['artist', 'songs']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['title']

class PlaylistSerializer(serializers.ModelSerializer):

    songs = SongAlbumViewSerializer()
    tags = TagSerializer()

    class Meta:
        model = Playlist
        fields = ['title', 'user_generated', 'songs', 'tags']
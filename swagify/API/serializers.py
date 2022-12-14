from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Artist, Genre, Song, Album, Playlist, Tag
from pprint import pprint as pp


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
        fields = [
            'name', 
            'listeners', 
            'bio'
            ]

class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = ['name']

class SongSerializer(serializers.ModelSerializer):

    main_artist = ArtistSerializer(many=True)

    feat_artist = ArtistSerializer(many=True)

    genre = GenreSerializer()

    class Meta:
        model = Song
        fields = [
            'title', 
            'main_artist', 
            'feat_artist', 
            'explicit', 
            'length',
            'plays', 
            'genre'
            ]

class AlbumSerializer(serializers.ModelSerializer):

    artist = serializers.SerializerMethodField()

    songs = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = [
            'title', 
            'artist', 
            'songs'
            ]

    def get_artist(self, obj):

        return obj.songs.first().main_artist.first().name

    def get_songs(self, obj):

        songs = obj.songs.all()

        album_song_view = []

        track_num = 1

        for song in reversed(songs):

            title = song.title

            feat_artists = song.feat_artist.all()

            feats = ''

            if feat_artists:

                f_a = []

                for x in feat_artists:
                    f_a.append(x.name)

                feats = f' feat. {(" ".join(f_a))}'

            album_song_view.append(f'Track {track_num}: {title}{feats}')

            track_num += 1

        return album_song_view


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['title']

class PlaylistSerializer(serializers.ModelSerializer):

    songs = SongSerializer(many=True)
    tags = TagSerializer(many=True )

    class Meta:
        model = Playlist
        fields = ['title', 'user_generated', 'songs', 'tags']
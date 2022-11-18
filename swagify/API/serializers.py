from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *
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

        this_album = obj.id

        songs = AlbumOrder.objects.filter(album=this_album)

        songID = songs.first().id

        artist = Song.objects.get(id=songID).main_artist.first().name

        return artist

    def get_songs(self, obj):

        this_album = obj.id

        songs = AlbumOrder.objects.filter(album=this_album)

        songs = [*songs.order_by('track_num')]

        tracklist = []

        for song in songs:

            songID = song.song.id

            feat_artist = [*Song.objects.get(id=songID).feat_artist.all()]

            feats = ''

            if feat_artist:
                f_a = []

                for x in feat_artist:
                    f_a.append(x.name)

                feats = f' feat. {(" ".join(f_a))}'

            sugg_pls =  PlaylistOrder.objects.filter(song=songID).all()

            appears = ''

            a_p = []

            if sugg_pls:

                for sugg in sugg_pls:
                
                
                    playlist = Playlist.objects.get(id=sugg.playlist.id).title
    
                    a_p.append(playlist)
    
                appears = f' (you might like these playlists! {(", ".join(a_p))})'

            tracklist.append(f'{song.track_num} {song.song.title}{feats}{appears}')

        return tracklist

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['title']

class PlaylistTitleSerializer(serializers.ModelSerializer):

    tags = TagSerializer()

    class Meta:
        model = Playlist
        fields = ['title', 'tags']

class PlaylistSerializer(serializers.ModelSerializer):

    songs = serializers.SerializerMethodField()

    tags = serializers.SerializerMethodField()

    class Meta:
        model = Playlist

        fields = [
            'title', 
            'user_generated', 
            'songs', 
            'tags'
            ]

    def get_songs(self, obj):

        this_playlist = obj.id

        songs = PlaylistOrder.objects.filter(playlist=this_playlist)

        songs = [*songs.order_by('track_num')]

        tracklist = []

        for song in songs:
            tracklist.append(f'{song.track_num} {song.song}')

        return tracklist
        
    def get_tags(self, obj):

        playlist_tags = obj.tags.all()

        tags = []

        for tag in playlist_tags:
            tags.append(tag.title)

        return tags
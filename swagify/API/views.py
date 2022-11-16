from django.shortcuts import render
from rest_framework import viewsets, permissions
from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from API.serializers import *
from django.contrib.auth.models import User, Group

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.AllowAny]

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [permissions.AllowAny]

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [permissions.AllowAny]

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [permissions.AllowAny]

class SongAPIView(APIView):

    def get_object(self, pk):
        try:
            return Song.objects.get(pk=pk)
        except Song.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):

        if pk:
            data = self.get_object(pk)
            serializers = SongSerializer(data)

        else:
            data = Song.objects.all()
            serializer = SongSerializer(data, many=True)

            return Response(serializer.data)

    def post(self, request, format=None):

        data = request.data

        serializer = SongSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message' : 'Song created successfully',
            'data': serializer.data,
        }

        return response

    def put(self, request, pk=None, format=None):
        song_to_update = Song.objects.get(pk=pk)
        data = request.data
        serializer = SongSerializer(instance=song_to_update, data=data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = Response()

        response = {
            'message': 'Song updated successfully',
            'data': serializer.data,
        }

        return response


class ArtistAPIView(APIView):

    def get_object(self, pk):
        try:
            return Artist.objects.get(pk=pk)
        except Artist.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):

        if pk:
            data = self.get_object(pk)
            serializers = ArtistSerializer(data)

        else:
            data = Artist.objects.all()
            serializer = ArtistSerializer(data, many=True)

            return Response(serializer.data)

    def post(self, request, format=None):

        data = request.data
        
        serializer = ArtistSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message' : 'Artist created successfully',
            'data': serializer.data,
        }

        return response
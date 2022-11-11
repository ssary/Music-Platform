import json

from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Artist
from .pagination import CustomPagination
from .serializers import ArtistSerializer
from django.shortcuts import render, redirect


class ArtistsView(APIView, CustomPagination):

    def get(self, request):
        artists = Artist.objects.all()
        results = self.paginate_queryset(artists, request, view=self)
        serializer = ArtistSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    # require login to create an artist
    def post(self, request):
        if request.user.is_authenticated:
            serilaizer = ArtistSerializer(data=request.data)
            if serilaizer.is_valid():
                serilaizer.save()
                return Response(serilaizer.data)
            else:
                return Response(serilaizer.errors)
        else:
            return redirect('/authentication/loginUser')


class ArtistView(APIView):
    def get(self, request, *args, **kwargs):
        artistId = kwargs['id']
        try:
            artistFetched = Artist.objects.get(id=artistId)
            serializer = ArtistSerializer(artistFetched)
            return Response(serializer.data)
        except IndexError:
            return Response(status=status.HTTP_404_NOT_FOUND)

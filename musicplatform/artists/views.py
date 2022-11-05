from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Artist
from .pagination import CustomPagination
from .serializers import ArtistSerializer

class ArtistsView(APIView, CustomPagination):
    def get(self, request):
        artists = Artist.objects.all()
        results = self.paginate_queryset(artists, request, view=self)
        serializer = ArtistSerializer(results, many=True)
        return Response(self.get_paginated_response(serializer.data))

    def post(self, request):
        serilaizer = ArtistSerializer(data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response(serilaizer.data)
        return Response(serilaizer.errors)

class ArtistView(APIView):
    def get(self, request, *args, **kwargs):
        artistId = kwargs['id']
        try:
            artistFetched = Artist.objects.get(id=artistId)
            serializer = ArtistSerializer(artistFetched)
            return Response(serializer.data)
        except IndexError:
            return Response(status=status.HTTP_404_NOT_FOUND)


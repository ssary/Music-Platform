from rest_framework import serializers
from .models import Artist
from albums.models import Album


class SecondAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['name', 'cost', 'isApproved']

    def create(self, validated_data):
        return Album.objects.create(**validated_data)


class ArtistSerializer(serializers.ModelSerializer):
    albums = SecondAlbumSerializer(many=True)
    class Meta:
        model=Artist
        fields = '__all__'

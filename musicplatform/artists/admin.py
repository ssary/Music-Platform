from django.contrib import admin
from .models import Artist
from albums.models import Album
from django import forms
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    readonly_fields = ['approved_albums']


#
# class AlbumForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(Album, self).__init__(*args, **kwargs)
#         super(Artist, self).__init__(*args, **kwargs)
#
#     class Meta:
#         model = Album
#         fields='__all__'
#
#
# class AlbumFormAdmin(admin.ModelAdmin):
#     form = AlbumForm
#
#
# admin.site.register(Artist, AlbumFormAdmin)
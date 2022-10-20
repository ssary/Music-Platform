from .models import Album
from django.contrib import admin
from django import forms


class AdminForm(forms.ModelForm):
    class Meta:
        model = Album
        help_texts = {'isApproved': 'Approve the album if its name is not explicit'}
        exclude = ()


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ['creation_date']
    form = AdminForm

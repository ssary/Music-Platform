import datetime

from django.db import models
from artists.models import Artist
from django.utils import timezone


class Album(models.Model):
    # when an artist is removed his albums is removed too
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, default='New Album')

    # aware of timezones: time zone is UTC
    creation_date = models.DateTimeField(default=timezone.now())
    released_date = models.DateTimeField(null=False)

    # Decimal preferred in currency as small calculation errors happen in float
    cost = models.DecimalField(null=False, decimal_places=4, max_digits=10)

    def __str__(self):
        return 'Album Name: {}'.format(self.name)

    def gg(self):
        for i in Artist.objects.all():
            i.album_set.all()
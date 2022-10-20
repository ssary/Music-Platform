from django.db import models


class Artist(models.Model):
    stage_name = models.CharField(null=False, unique=True, max_length=100)
    social_link = models.URLField(max_length=128, unique=True)
    approved_albums = models.IntegerField()
    class Meta:
        db_table = 'artist'
        ordering = ['stage_name']

    def __str__(self):
        return 'artist name: {} social Media Link: {}'.format(self.stage_name, self.social_link)


    def save(self, *args, **kwargs):
        self.approved_albums = self.album_set.filter(isApproved=True).count()
        super(Artist, self).save(*args, **kwargs)

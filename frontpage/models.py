from django.db import models
from frontpage.storage_backends import PublicMediaStorage


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(storage=PublicMediaStorage())

    class Meta:
        db_table = "image"


class Actuality(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    stop_date = models.DateField()
    article = models.TextField(max_length=1000)
    short_desc = models.TextField(max_length=110)
    img_title = models.CharField(max_length=400)
    format = models.BooleanField(default=0)
    external_link = models.CharField(max_length=300)
    state = models.BooleanField(default=1)

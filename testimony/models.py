from django.db import models


class Testimony(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=100)
    promotion = models.CharField(max_length=100)
    job = models.TextField()
    sector = models.CharField(max_length=100)
    state = models.BooleanField(default=1)

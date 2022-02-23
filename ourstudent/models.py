from django.db import models


class Promotion(models.Model):
    state = models.BooleanField(default=1)
    img_link = models.CharField(max_length=1000, default="")
    formation = models.CharField(max_length=200, default="")
    date = models.CharField(max_length=30, default="")
    col1 = models.CharField(max_length=2000, default="")
    col2 = models.CharField(max_length=2000, default="")
    col3 = models.CharField(max_length=2000, default="")

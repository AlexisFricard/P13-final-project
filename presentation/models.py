from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=500, default="#")
    img_link = models.CharField(max_length=500)
    status1 = models.CharField(max_length=250, default="")
    status2 = models.CharField(max_length=250, default="")
    status3 = models.CharField(max_length=250, default="")
    status4 = models.CharField(max_length=250, default="")
    status5 = models.CharField(max_length=250, default="")
    grade = models.CharField(max_length=50)
    state = models.BooleanField(default=1)

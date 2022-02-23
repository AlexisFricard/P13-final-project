from django.db import models


class MemberOffice(models.Model):
    name = models.CharField(max_length=100, default="")
    role = models.CharField(max_length=100, default="")
    link = models.CharField(max_length=100, default="")
    img_link = models.CharField(max_length=100, default="")
    promotion = models.CharField(max_length=20, default="")
    genre = models.CharField(max_length=1, default="n")

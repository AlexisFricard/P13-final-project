from django.db import models


class Faq(models.Model):
    question = models.CharField(max_length=200)
    response = models.TextField()
    state = models.BooleanField(default=1)


class Link(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    state = models.BooleanField(default=1)

from django.db import models
from frontpage.storage_backends import PublicMediaStorage


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(storage=PublicMediaStorage())

    class Meta:
        db_table = "image"


class Faq(models.Model):
    question = models.CharField(max_length=200)
    response = models.TextField()


class Link(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=400)


class Actuality(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    stop_date = models.DateField()
    article = models.TextField()
    img_title = models.CharField(max_length=400)


class Testimony(models.Model):
    text = models.TextField()
    author = models.TextField()
    sector = models.CharField(max_length=100)


class Promotion(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    img_title = models.CharField(max_length=200)


class Ticket(models.Model):
    title = models.CharField(max_length=29)
    state = models.BooleanField(default=1)
    author = models.CharField(max_length=200)


class AuthorMessageTicket(models.Model):
    author = models.CharField(max_length=200)
    message = models.TextField()
    ticket_id = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

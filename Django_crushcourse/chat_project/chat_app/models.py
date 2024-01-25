from django.db import models
from datetime import datetime
# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=100)


class Message(models.Model):
    message = models.CharField(max_length=1000)
    date = models.DateTimeField(default=datetime.now())
    user = models.CharField(max_length=1_000_000)
    room = models.CharField(max_length=1_000_000)

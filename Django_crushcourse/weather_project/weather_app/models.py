from django.db import models

# Create your models here.

class Weather(models.Model):
    city = models.CharField(max_length=100)
    country_code = models.CharField(max_length=100)
    coordinates = models.CharField(max_length=100)
    temperature = models.CharField(max_length=4)
    pressure = models.CharField(max_length=4)
    humidity = models.CharField(max_length=4)



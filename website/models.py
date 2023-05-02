from django.db import models


# Create your models here.

class Slider(models.Model):
    subtitle = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    bottom_subtitle = models.CharField(max_length=250)
    button_text = models.CharField(max_length=50)
    button_url = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)


class Service(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='services/')
    desc = models.CharField(max_length=250)

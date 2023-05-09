import uuid

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


class Package(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name

    @property
    def get_features(self):
        return self.feature_set.all()


class Feature(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)


class Video(models.Model):
    youtube = models.CharField(max_length=150)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    website = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Subscriber(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    website = models.CharField(max_length=100)

    def __str__(self):
        return self.email


class WebsiteSettings(models.Model):
    site_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='settings/')
    about_title = models.CharField(max_length=100)
    about_desc = models.TextField()
    project_no = models.IntegerField(default=1)
    website_no = models.IntegerField(default=1)
    client_no = models.IntegerField(default=1)
    project_desc = models.CharField(max_length=100)
    website_desc = models.CharField(max_length=100)
    client_desc = models.CharField(max_length=100)
    about_image = models.ImageField(upload_to='settings/')
    facebook = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    behance = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.site_name

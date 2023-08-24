from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class MenuItem(models.Model):
    # Model for menu items
    title = models.CharField(max_length=30, unique=True)
    description = models.TextField(default="")
    featured_image = CloudinaryField('image', default='placeholder')
    price = models.FloatField(default=0.00)
    vegan = models.BooleanField(default=False)

    class Meta:
        # Order by name
        ordering = ['title']

    def __str__(self):
        return str(self.title)


class Menu(models.Model):
    # Model to create a menu
    title = models.CharField(max_length=25, unique=True)
    cakes = models.ManyToManyField('MenuItem', related_name='cakes')
    pastry = models.ManyToManyField('MenuItem', related_name='pastry')

    class Meta:
        # Order by name
        ordering = ['title']

    def __str__(self):
        return str(self.title)

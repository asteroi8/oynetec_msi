from django.db import models

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=200)

class Country(models.Model):
    locode = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.locode

class Location(models.Model):
    locode = models.CharField(max_length=10)
    name = models.CharField(max_length=200, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Site(models.Model):
    name = models.CharField(max_length=200, unique=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

import os

def get_image_path(instance, filename):
    return os.path.join(BASE_DIR, MEDIA_ROOT, str(instance.id), filename) 
    return os.path.join('photos', str(instance.id), filename)

class SitePicture(models.Model):
    #user = models.ForeignKey(User, unique=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='site_image', blank=True, null=True)
    def __str__(self):
        return str(self.site)

class System(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

#from djangotoolbox.fields import ListField
class Component(models.Model):
    name = models.CharField(max_length=200)
    manufacturer =  models.ForeignKey(Supplier, on_delete=models.CASCADE) 
    model = models.CharField(max_length=200)
    serial = models.CharField(max_length=200)
    system = models.ForeignKey(System, on_delete=models.CASCADE) 
    def __str__(self):
        return self.name
#class Software(models.Model):
   # name = models.CharField(max_length=200)
  #  vendor = models.CharField(max_length=200)
 #   model = models.CharField(max_length=200)
#    serial = models.CharField(max_length=200)

class Install(models.Model):
    what = models.ForeignKey(Component, on_delete=models.CASCADE) 
    when = models.DateTimeField()
    where = models.ForeignKey(Site, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.what)

class Node(models.Model):
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    hostname = models.CharField(max_length=200)
    ipv4 = models.CharField(max_length=200, blank=True)
    ipv6 = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.hostname


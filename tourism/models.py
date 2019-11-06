from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class attractions(models.Model):
    name=models.CharField(max_length=100)
    image=models.CharField(max_length=200)
    img = ArrayField(models.CharField(max_length=1000, blank=True))
    description = ArrayField(models.CharField(max_length=10000, blank=True))
    latitude = models.FloatField()
    longitude = models.FloatField()
    district = models.CharField(max_length=20,default='Kathmandu')
    province = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class hotels(models.Model):
    name=models.CharField(max_length=100)
    img = ArrayField(models.CharField(max_length=1000, blank=True),null=True)
    district=models.CharField(max_length=100)
    province=models.IntegerField(default=1)
    place=models.CharField(max_length=100)
    star=models.CharField(max_length=100)
    cost=models.CharField(max_length=100)
    description=models.CharField(max_length=10000)
    amenities=ArrayField(models.CharField(max_length=10000, blank=True))
    url=models.URLField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

class festivals(models.Model):
    name=models.CharField(max_length=100)
    image=models.CharField(max_length=200)
    img=ArrayField(models.CharField(max_length=1000, blank=True))
    description = ArrayField(models.CharField(max_length=10000, blank=True))

    def __str__(self):
        return self.name

class cafe(models.Model):
    name=models.CharField(max_length=100)
    image=models.CharField(max_length=200)
    img=ArrayField(models.CharField(max_length=1000, blank=True))
    description = models.CharField(max_length=10000)
    district=models.CharField(max_length=100)
    province=models.IntegerField(default=1)
    place=models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

class pubs(models.Model):
    name=models.CharField(max_length=100)
    image=models.CharField(max_length=200)
    img=ArrayField(models.CharField(max_length=1000, blank=True))
    description = models.CharField(max_length=10000)
    district=models.CharField(max_length=100)
    province=models.IntegerField(default=1)
    place=models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    phone = models.CharField(max_length=15,null=True)

    def __str__(self):
        return self.name

class restaurants(models.Model):
    name=models.CharField(max_length=100)
    image=models.CharField(max_length=200)
    img = ArrayField(models.CharField(max_length=1000, blank=True))
    district=models.CharField(max_length=100)
    province=models.IntegerField(default=1)
    place=models.CharField(max_length=100)
    description=models.CharField(max_length=10000)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

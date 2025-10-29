from django.db import models 
from django.contrib.auth.models import User

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=10 , blank=True, null=True)

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    origin = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
      return self.name


   

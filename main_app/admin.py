from django.contrib import admin 
from .models import Dish, Location

# Register your models here.

admin.site.register(Dish)
admin.site.register(Location)
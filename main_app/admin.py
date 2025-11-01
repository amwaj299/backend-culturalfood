from django.contrib import admin 
from .models import Dish , Location  , Tag

# Register your models here.

admin.site.register(Dish)
admin.site.register(Location)
admin.site.register(Tag)

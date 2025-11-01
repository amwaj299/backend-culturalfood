from django.db import models 
from django.contrib.auth.models import User

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    origin = models.ForeignKey(Location, on_delete=models.CASCADE)
    photo = models.URLField(blank=True)

    def __str__(self):
      return self.name


    # def create(self, validated_data):
    #     user = self.context['request'].user
    #     dish = Dish.objects.create(user=user, **validated_data)
    #     return dish



# class Photo(models.Model):
#     url = models.TextField()
#     title = models.CharField(max_length=250)
#     created_at = models.DateField(auto_now_add=True)
#     updated_at = models.DateField(auto_now=True)
#     dish = models.OneToOneField(Dish, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"Photo for dish_id: {self.dish.id} @{self.url}"

   

from rest_framework import serializers
from .models import Dish , Location


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = "__all__"



class DishSerializer(serializers.ModelSerializer):
    origin = LocationSerializer(read_only=True)
    origin_id = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.all(),
        source='origin',
        write_only=True
    )

    class Meta:
        model = Dish
        fields = ['id', 'name', 'description', 'photo', 'origin', 'origin_id']

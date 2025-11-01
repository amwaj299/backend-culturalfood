from rest_framework import serializers
from .models import Dish , Location , Tag


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = "__all__"

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class DishSerializer(serializers.ModelSerializer):
    origin = LocationSerializer(read_only=True)
    origin_id = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.all(),
        source='origin',
        write_only=True
    )
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Dish
        fields = ['id', 'name', 'description', 'photo', 'origin', 'origin_id', 'user', 'tags']


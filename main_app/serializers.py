from rest_framework import serializers
from .models import Dish, Location, Tag
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


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
    user = serializers.PrimaryKeyRelatedField(read_only=True)  
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Dish
        fields = ['id', 'name', 'description', 'photo', 'origin', 'origin_id', 'user', 'tags']


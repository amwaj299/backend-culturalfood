from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

class Home(APIView):
    def get(self, request):
        return Response({'message': 'Welcome to Cultural Food API!'})

class Dishes(APIView):

    def get(self, request):
        sample_dishes = [
            {'name': 'Kabsa', 'origin': 'Saudi', 'description': 'Spiced rice with meat.'},
            {'name': 'Sushi', 'origin': 'Japan', 'description': 'Fresh fish with rice.'},
            {'name': 'Tacos', 'origin': 'Mexico', 'description': 'Tortilla with fillings.'},
        ]
        return Response({'dishes': sample_dishes})


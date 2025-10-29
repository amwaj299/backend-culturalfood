from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

class Home(APIView):
    def get(self, request):
        return Response({'message': 'Welcome to Cultural Food API!'})

# class Dishes(APIView):
   
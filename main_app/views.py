from django.shortcuts import render
# Create your views here.
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Dish
from .serializers import DishSerializer

# class DisheIndex(APIView):
#     def get(self, request):
#         return Response({'message': 'This is the Dishes Index'})

class Home(APIView):
    def get(self, request):
        return Response({'message': 'Welcome to Cultural Food API!'})

class Dishes(APIView):
    serializer_class = DishSerializer

    def get(self, request):
        try:
            queryset = Dish.objects.all()
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


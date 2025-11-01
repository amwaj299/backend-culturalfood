from django.shortcuts import render, get_object_or_404
from rest_framework import generics,status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Dish , Location , Tag
from .serializers import DishSerializer , LocationSerializer , TagSerializer





class Home(APIView):
    def get(self, request):
        return Response({'message': 'Welcome to Cultural Food API!'})

class DishesIndex(APIView):
    serializer_class = DishSerializer

    def get(self, request):
        queryset = Dish.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        data['user'] = 1
        serializer = self.serializer_class(data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DishDetail(APIView):
    serializer_class = DishSerializer

    def get(self, request, dish_id):
        dish = get_object_or_404(Dish, id=dish_id)
        serializer = self.serializer_class(dish)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, dish_id):
        dish = get_object_or_404(Dish, id=dish_id)
        serializer = self.serializer_class(dish, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, dish_id):
        dish = get_object_or_404(Dish, id=dish_id)
        dish.delete()
        return Response({'success': True}, status=status.HTTP_200_OK)


class LocationDishes(APIView):
    serializer_class = DishSerializer

    def get(self, request, location_id):
        try:
            queryset = Dish.objects.filter(origin=location_id)
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class LocationsIndex(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer



class TagListCreate(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer




# class PhotoDetail(APIView):
#     serializer_class = PhotoSerializer

#     def post(self, request, dish_id):
#         try:
#             data = request.data.copy()
#             data["dish"] = int(dish_id)

#             existing_photo = Photo.objects.filter(dish=dish_id)
#             if existing_photo:
#                 existing_photo.delete()

#             serializer = self.serializer_class(data=data)
#             if serializer.is_valid():
#                 dish = get_object_or_404(Dish, id=dish_id)
#                 serializer.save()
#                 return Response(DishSerializer(dish).data, status=status.HTTP_200_OK)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Exception as err:
#             return Response({"error": str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)






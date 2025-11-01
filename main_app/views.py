from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status , permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Dish, Location, Tag
from .serializers import DishSerializer, LocationSerializer, TagSerializer , UserSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class Home(APIView):
    def get(self, request):
        return Response({'message': 'Welcome to Cultural Food API!'})


class DishesIndex(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DishSerializer

    def get(self, request):
        queryset = Dish.objects.filter(user=request.user)
        serializer = DishSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user_id=request.user.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DishDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DishSerializer

    def get(self, request, dish_id):
        dish = get_object_or_404(Dish, id=dish_id)
        serializer = self.serializer_class(dish)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, dish_id):
        dish = get_object_or_404(Dish, id=dish_id)
        serializer = self.serializer_class(dish, data=request.data, context={'request': request})

        if serializer.is_valid():
            updated_dish = serializer.save()

            tag_ids = request.data.get('tag_ids', [])
            if isinstance(tag_ids, list) and len(tag_ids) > 0:
                updated_dish.tags.set(tag_ids)

            updated_dish.refresh_from_db()
            dish_data = DishSerializer(updated_dish, context={'request': request}).data
            return Response(dish_data, status=status.HTTP_200_OK)

        print("Serializer Errors:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LocationDishes(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DishSerializer

    def get(self, request, location_id):
        try:
            queryset = Dish.objects.filter(origin=location_id)
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class FilteredDishes(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DishSerializer

    def get(self, request, tag_name):
        try:
            tag = get_object_or_404(Tag, name=tag_name)
            queryset = Dish.objects.filter(tags=tag)
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LocationsIndex(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class TagListCreate(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LoginView(APIView):
    def post(self, request):
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                refresh = RefreshToken.for_user(user)
                content = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'user': UserSerializer(user).data
                }
                return Response(content, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class VerifyUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            user = User.objects.get(username=request.user.username)
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data
            }, status=status.HTTP_200_OK)
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



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






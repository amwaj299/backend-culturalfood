from django.urls import path 
from .views import Home, DishesIndex , DishDetail  , LocationDishes , LocationsIndex ,TagListCreate

urlpatterns = [

    path('', Home.as_view(), name='home'),
    path('dishes/', DishesIndex.as_view(), name='dish-index'),
    path('dishes/<int:dish_id>/', DishDetail.as_view(), name='dish-detail'),
    path('locations/<int:location_id>/dishes/', LocationDishes.as_view(), name='location-dishes'),
    path('locations/', LocationsIndex.as_view(), name='location-index'),
    path('tags/',TagListCreate.as_view(), name='tag-list-create'),
 
]



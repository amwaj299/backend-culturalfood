from django.urls import path 
from .views import Home, Dishes , DishDetail

urlpatterns = [

    path('', Home.as_view(), name='home'),
    path('dishes/', Dishes.as_view(), name='dish-index'),
    path('dishes/<int:dish_id>/', views.DishDetail.as_view(), name='dish-detail'),
]

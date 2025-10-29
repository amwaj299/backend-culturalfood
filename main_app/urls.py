from django.urls import path
from .views import Home, Dishes

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('dishes/', Dishes.as_view(), name='dish-index'),
]

from django.urls import path
from . import views

urlpatterns = [
  path('wines/', views.wine_list, name='wine_list'),
  path('wines/<int:pk>', views.wine_detail, name='wine_detail'),
  path('food/', views.food_list, name='food_list'),
  path('food/<int:pk>', views.food_detail, name='food_detail')
]
from django.shortcuts import render

from .models import Food, Wine, User, Pairing, Favorite

from django.contrib.auth.decorators import login_required

from rest_framework import generics
from .serializers import FoodSerializer, WineSerializer, UserSerializer, PairingSerializer, FavoriteSerializer

class WineList(generics.ListCreateAPIView):
  queryset = Wine.objects.all()
  serializer_class = WineSerializer

class WineDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Wine.objects.all()
  serializer_class = WineSerializer

class FoodList(generics.ListCreateAPIView):
  queryset = Food.objects.all()
  serializer_class = FoodSerializer

class FoodDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Food.objects.all()
  serializer_class = FoodSerializer


# Create your views here.

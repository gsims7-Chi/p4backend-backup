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


####### WINE #######

# Wine Index

def wine_list(request):
  wines = Wine.objects.all()
  return render(request, 'any_day_sommelier/wine_list.html', {'wines': wines})

# Wine Show

def wine_detail(request, pk):
  wine = Wine.objects.get(id=pk)
  return render(request, 'any_day_sommelier/wine_detail.html', {'wine': wine})

####### FOOD #######

# Food Index

def food_list(request):
  food = Food.objects.all()
  return render(request, 'any_day_sommelier/food_list.html', {'food': food})

# Food Show

def food_detail(request, pk):
  food = Food.objects.get(id=pk)
  return render(request, 'any_day_sommelier/food_detail.html', {'food': food})

####### PAIRING #######

def pairing_list(request):
  pairings = Pairing.objects.all()
  return render(request, 'any_day_sommelier/pairing_list.html', {'pairing': pairing})



  

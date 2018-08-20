from django import forms
from .models import Wine, Food, User, Pairing, Favorite

class WineForm(forms.ModelForm):
  class Meta:
    model = Wine
    fields = ('type')

class FoodForm(forms.ModelForm):
  class Meta:
    model = Food
    fields = ('entree', 'main_ingredient')

class UserForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ('username', 'password')

class PairingForm(forms.ModelForm):
  class Meta:
    model = Pairing
    fields = ('wine', 'food')

class FavoriteForm(forms.ModelForm):
  class Meta:
    model = Favorite
    fields = ('user', 'pairing')
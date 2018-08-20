from django.db import models

class Wine(models.Model):
  type = models.CharField(max_length=100)

  def __str__(self):
    return self.type

class Food(models.Model):
  entree = models.CharField(max_length=100)
  main_ingredient = models.CharField(max_length=100)

  def __str__(self):
    return self.entree

class User(models.Model):
  username = models.CharField(max_length=100)
  password = models.CharField(max_length=100)

  def __str__(self):
    return self.username

class Pairing(models.Model):
  wine = models.ForeignKey(Wine, on_delete=models.CASCADE, related_name='pairings')
  food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='pairings')

  def __str__(self):
    return self.wine

class Favorite(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
  pairing = models.ForeignKey(Pairing, on_delete=models.CASCADE, related_name='favorites')

  def __str__(self):
    return self.user


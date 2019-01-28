from django.db import models

# Create your models here.

class Jugador(models.Model):
    nomJugador = models.CharField(max_length=50, primary_key=True)
    numFormatges = models.IntegerField()
    numFormatgets = models.IntegerField()
    email = models.CharField(200)
    password = models.CharField(50)
    def __str__(self):
        return self.nomJugador

class Skin(models.Model):
    nomSkin = models.CharField(max_length=50)
    preu = models.IntegerField()
    def __str__(self):
        return self.nomSkin

class SkinComprada(models.Model):
    nomJugador = models.ForeignKey(Jugador, primary_key=True)
    nomSkin = models.ForeignKey(Skin, primary_key=True)
    posada = models.BooleanField()
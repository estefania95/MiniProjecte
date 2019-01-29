from django.db import models

# Create your models here.

class Jugador(models.Model):
    nomJugador = models.CharField(max_length=50, primary_key=True, )
    numFormatges = models.IntegerField()
    numFormatgets = models.IntegerField()
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.nomJugador

class Skin(models.Model):
    nomSkin = models.CharField(max_length=50)
    preu = models.IntegerField()
    def __str__(self):
        return self.nomSkin

class SkinComprada(models.Model):
    nomJugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    nomSkin = models.ForeignKey(Skin, on_delete=models.CASCADE)
    posada = models.BooleanField()
    class Meta:
        unique_together = (("nomJugador", "nomSkin"),)
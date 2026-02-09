from django.db import models

# Create your models here.

class Equipos(models.Model):
  tipo = models.CharField()
  marca = models.CharField()
  modelo = models.CharField()
  numero_serie = models.CharField()


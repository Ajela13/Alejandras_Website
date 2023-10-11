from django.db import models

# Create your models here.

class Dane(models.Model):
    DEPARTAMENTO =models.CharField(max_length=100)
    MUNICIPIO=models.CharField(max_length=100)
    CODIGO_DANE=models.CharField(max_length=100)
    ARMAS_MEDIOS=models.CharField(max_length=100)
    FECHA_HECHO=models.DateField()
    GENERO=models.CharField(max_length=100)
    GRUPO_ETARIO=models.CharField(max_length=100)
    CANTIDAD=models.IntegerField()
    

class Geojason(models.Model):
    type=models.CharField(max_length=255)
    crs=models.JSONField()
    features=models.JSONField()


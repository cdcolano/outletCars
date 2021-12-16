
from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import ManyToManyField

# Create your models here



class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    pais= models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nombre


class Categoría(models.Model):
    # Campo para la relación
    nombre = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nombre

class Motor(models.Model):
    nombre = models.CharField(max_length=50)
    combustible = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.nombre
class Coche(models.Model):
    modelo = models.CharField(max_length=50)
    matricula = models.CharField(max_length=9, primary_key=True)
    precio=models.IntegerField()
    cv=models.IntegerField()
    km=models.BigIntegerField()
    marca=models.ForeignKey(Marca, on_delete=models.CASCADE)
    motor= models.ForeignKey(Motor, on_delete=models.CASCADE)
    categoría=models.ManyToManyField(Categoría)
    imagen= models.ImageField(upload_to='static/img/')
    def __str__(self) -> str:
        return self.matricula
    class Meta:
        ordering=['precio']




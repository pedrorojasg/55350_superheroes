from django.db import models


class Heroe(models.Model):
    nombre = models.CharField(max_length=256)
    nombre_real = models.CharField(max_length=256)
    residencia = models.CharField(max_length=256)
    fecha_nacimiento = models.DateField(null=True)
    peso = models.IntegerField(null=True)


class Villano(models.Model):
    nombre = models.CharField(max_length=256)
    nombre_real = models.CharField(max_length=256)
    residencia = models.CharField(max_length=256)
    fecha_nacimiento = models.DateField(null=True)
    peso = models.IntegerField(null=True)


class Poder(models.Model):
    nombre = models.CharField(max_length=256)
    descripcion = models.TextField()

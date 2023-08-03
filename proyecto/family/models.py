from django.db import models

# Create your models here.
class Familiar(models.Model):
    nombres =           models.CharField(max_length=50)
    apellidos =         models.CharField(max_length=50)
    fechaNacimiento =   models.DateField()
    DNI =               models.IntegerField()
    nombres_madre =     models.CharField(max_length=50)
    apellidos_madre =   models.CharField(max_length=50)
    nombres_padre =     models.CharField(max_length=50)
    apellidos_padre =   models.CharField(max_length=50)

from django.db import models

# Create your models here.

class Genero(models.Model):
    nombre = models.CharField(max_length=20)

class Pais(models.Model):
    nombre = models.CharField(max_length=30)

class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    bio = models.CharField(max_length=2000)
    nacionalidad = models.ForeignKey(Pais, on_delete=models.CASCADE)

class Editorial(models.Model):
    nombre = models.CharField(max_length=30)
    ubicacion = models.ForeignKey(Pais, on_delete=models.CASCADE)

class Libro(models.Model):
    nombre = models.CharField(max_length=30)
    sinopsis = models.CharField(max_length=2000)
    paginas = models.IntegerField()

    precio = models.FloatField(default=0)
    descuento = models.FloatField(default=1)
    ISBN = models.CharField(max_length=13)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)






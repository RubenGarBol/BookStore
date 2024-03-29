from django.db import models

# Create your models here.

class Genero(models.Model):
    nombre = models.CharField(max_length=20)

class Pais(models.Model):
    nombre = models.CharField(max_length=30)

class Idioma(models.Model):
    idioma = models.CharField(max_length=30)

class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    bio = models.CharField(max_length=2000)
    nacionalidad = models.ForeignKey(Pais, on_delete=models.CASCADE, default=1)

class Editorial(models.Model):
    nombre = models.CharField(max_length=30)
    ubicacion = models.ForeignKey(Pais, on_delete=models.CASCADE, default=1)

class Libro(models.Model):
    nombre = models.CharField(max_length=30)
    sinopsis_min = models.CharField(max_length=200,default="")
    sinopsis_max = models.CharField(max_length=2000,default="")
    paginas = models.IntegerField()
    linkPortada = models.CharField(max_length=1000, default="")
    precio = models.FloatField(default=0)
    descuento = models.FloatField(default=1)
    ISBN = models.CharField(max_length=13)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, default=1)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, default=1)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    fecha = models.IntegerField(default=0)
    destacado = models.IntegerField(default=0)
    idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE, default=1)
    ventas = models.IntegerField(default=0)
    promocionado = models.BooleanField(default=0)

class Usuario(models.Model):
	email = models.CharField(max_length=200)
	contraseña = models.CharField(max_length=200)
	nombre = models.CharField(max_length=200, default="")

class Deseado(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=1)
	libro = models.ForeignKey(Libro, on_delete=models.CASCADE)

class MensajesContacto(models.Model):
    email = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    mensaje = models.CharField(max_length=30)

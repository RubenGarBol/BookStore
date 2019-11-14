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
    nacionalidad = models.ForeignKey(Pais, on_delete=models.CASCADE)

class Editorial(models.Model):
    nombre = models.CharField(max_length=30)
    ubicacion = models.ForeignKey(Pais, on_delete=models.CASCADE)

class Libro(models.Model):
    nombre = models.CharField(max_length=30)
    sinopsis = models.CharField(max_length=2000)
    paginas = models.IntegerField()
    linkPortada = models.CharField(max_length=1000, default="")
    precio = models.FloatField(default=0)
    descuento = models.FloatField(default=1)
    ISBN = models.CharField(max_length=13)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE)
    ventas = models.IntegerField()
    #Si el valor es 1, 2 o 3 el libro se promocionara en el slider de la pagina web
    promocionado = model.IntegerField()

class Usuario(models.Model):
	email = models.CharField(max_length=200)
	contraseña = models.CharField(max_length=200)
	nombre = models.CharField(max_length=200, default="")

class Deseado(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	libro = models.ForeignKey(Libro, on_delete=models.CASCADE)

class MensajesContacto(models.Model):
    email = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    mensaje = models.CharField(max_length=30)


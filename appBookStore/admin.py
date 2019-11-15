from django.contrib import admin
from appBookStore.models import Genero, Pais, Autor, Editorial, Libro, Usuario, Deseado, Idioma, MensajesContacto
# Register your models here.
admin.site.register(Genero)
admin.site.register(Pais)
admin.site.register(Autor)
admin.site.register(Editorial)
admin.site.register(Libro)
admin.site.register(Usuario)
admin.site.register(Idioma)
admin.site.register(Deseado)
admin.site.register(MensajesContacto)

from django.contrib import admin
from appBookStore.models import Genero, Pais, Autor, Editorial, Libro
# Register your models here.
admin.site.register(Genero)
admin.site.register(Pais)
admin.site.register(Autor)
admin.site.register(Editorial)
admin.site.register(Libro)
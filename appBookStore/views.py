from django.shortcuts import render, HttpResponse, get_object_or_404, get_list_or_404, redirect
from appBookStore.models import Libro, MensajesContacto, Autor, Usuario
from appBookStore.forms import Contacto, Registro

from django.conf import settings

def index(request):
	lista_libros = Libro.objects.filter().order_by('-fecha')
	lista_ventas = Libro.objects.filter().order_by('ventas')
	#Crear un context	
	context = {
		"lista_libros": lista_libros,
		"lista_ventas": lista_ventas,
	}
	return render(request, 'index.html', context)

def examples(request):
    return render(request, "appBookStore/examples.html",)

def a_page(request):
    return render(request, "appBookStore/page.html",)

def another_page(request):
    return render(request, "appBookStore/another_page.html",)

def contact(request):
    context = {"form": Contacto}
    return render(request, 'contact.html', context)

def register(request):
    context = {"form": Registro}
    return render(request, 'register.html', context)

def login(request):
    return render(request, "login.html",)

def details(request, ID):
    obj = Libro.objects.get(id=ID)
    context = {
        'titulo': obj.nombre,
        'sinopsis_min': obj.sinopsis_min,
        'sinopsis_max': obj.sinopsis_max,
        'paginas': obj.paginas,
        'linkPortada': obj.linkPortada,
        'precio': obj.precio,
        'ISBN': obj.ISBN,
        'genero': obj.genero,
        'editorial': obj.editorial,
        'idioma': obj.idioma,
        'autor': obj.autor,
        'genero': obj.genero
    }
    return render(request, "details.html", context)


def addMensaje(request):
    form = Contacto(request.POST)

    if form.is_valid():
        msj = MensajesContacto(email = form.cleaned_data['email'], nombre = form.cleaned_data['nombre'], mensaje = form.cleaned_data['mensaje'])
        msj.save()

    return redirect('home')

def addUser(request):
    form = Registro(request.POST)

    if form.is_valid():
        register = Usuario(nombre = form.cleaned_data['usuario'], contraseña = form.cleaned_data['contraseña'], email = form.cleaned_data['email'])
        register.save()

    return redirect('home')

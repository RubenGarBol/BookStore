from django.shortcuts import render, HttpResponse, get_object_or_404, get_list_or_404, redirect
from appBookStore.models import Libro, MensajesContacto
from appBookStore.forms import Contacto

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

def addMensaje(request):
    form = Contacto(request.POST)

    if form.is_valid():
        msj = MensajesContacto(email = form.cleaned_data['email'], nombre = form.cleaned_data['nombre'], mensaje = form.cleaned_data['mensaje'])
        msj.save()

    return redirect('home')
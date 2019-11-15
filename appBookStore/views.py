from django.shortcuts import render, HttpResponse, get_object_or_404, get_list_or_404
from appBookStore.models import Libro
from django.conf import settings

def index(request):
	lista_libros = Libro.objects.filter().order_by('fecha')
	#Crear un context	
	context = {
		"lista_libros": lista_libros,
	}
	return render(request, 'index.html', context)

def examples(request):
    return render(request, "appBookStore/examples.html",)

def a_page(request):
    return render(request, "appBookStore/page.html",)

def another_page(request):
    return render(request, "appBookStore/another_page.html",)

def contact(request):
    return render(request, "appBookStore/contact.html",)

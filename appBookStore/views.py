from django.shortcuts import render, HttpResponse, get_object_or_404, get_list_or_404
from appBookStore.models import Libro
from django.conf import settings

def index(request):
	lista_libros = Libro.objects.all()
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

def addMensaje(request):
    form = ContactForm(request.POST)

    if form.is_valid():
        msj = MensajesContacto(email = form.cleaned_data['email'], nombre = form.cleaned_data['name'], mensaje = form.cleaned_data['message'])
        msj.save()

    return redirect('home')
from django.shortcuts import render

def index(request):
    return render(request, "index.html",)

def examples(request):
    return render(request, "appBookStore/examples.html",)

def a_page(request):
    return render(request, "appBookStore/page.html",)

def another_page(request):
    return render(request, "appBookStore/another_page.html",)

def contact(request):
    return render(request, "appBookStore/contact.html",)

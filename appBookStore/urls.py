from django.urls import path
from . import views

urlpatterns = [
 path('bookstore/', views.index, name='home'),
 path('bookstore/examples', views.examples, name='examples'),
 path('bookstore/a_page', views.a_page, name='a_page'),
 path('bookstore/another_page', views.another_page, name='another_page'),
 path('bookstore/contact', views.contact, name='contact'),
path('bookstore/addMensaje/', views.addMensaje, name='addMensaje')
]

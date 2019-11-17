from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='home'),
	path('examples', views.examples, name='examples'),
	path('contact', views.contact, name='contact'),
	path('register', views.register, name='register'),
	path('login', views.login, name='login'),
	path('details/<ID>', views.details, name='details'),
	path('addMensaje/', views.addMensaje, name='addMensaje'),
	path('addUser/', views.addUser, name='addUser')
]

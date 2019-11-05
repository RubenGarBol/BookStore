from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='home'),
 path('examples', views.examples, name='examples'),
 path('a_page', views.a_page, name='a_page'),
 path('another_page', views.another_page, name='another_page'),
 path('contact', views.contact, name='contact'),
]

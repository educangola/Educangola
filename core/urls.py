from django.contrib import admin
from django.urls import path, include
from usuarios import views as viewhome
from core import views as viewerro



urlpatterns = [
    path('home', viewhome.home, name = "home" ),
    path('erro/', viewerro.Erro, name = "erro"),
    

]
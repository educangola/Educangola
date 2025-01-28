from django.contrib import admin
from django.urls import path, include
from usuarios import views

urlpatterns = [
    path('categorias/<int:id>/', views.cursos_por_categoria, name='cursos_por_categoria'),
]

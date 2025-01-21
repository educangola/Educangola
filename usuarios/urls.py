from django.contrib import admin
from django.urls import path, include
from usuarios import views

urlpatterns = [
    path('Cadastrar_normal/', views.Cadastrar_normal, name="Cadastrar_normal" ),
    path('Login_normal/', views.Login_normal, name="Login_normal" ),
    path('categorias/<int:id>/', views.cursos_por_categoria, name='cursos_por_categoria'),
    path('Valida_cadastro_normal/', views.Valida_cadastro_normal, name='Valida_cadastro_normal'),
    path('Valida_login_normal/', views.Valida_login_normal, name='Valida_login_normal'),    
]
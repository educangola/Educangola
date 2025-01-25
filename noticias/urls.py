from django.contrib import admin
from django.urls import path, include
from noticias import views
urlpatterns = [
    path('noticia/', views.noticia, name = 'noticia'),
    path('noticia/<int:id>/', views.noticia_detalhe, name='noticia_detalhe'),
    path('noticia/categoria/<int:categoria_id>/', views.noticia_por_categoria, name='noticia_por_categoria'),
    path('recente_news/', views.recente_news, name = 'recente_news'),
    
]
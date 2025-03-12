from django.contrib import admin
from django.urls import path, include
from instituicoes import views

urlpatterns = [
    path('detalhe_instituicao/<int:id>', views.detalhe_instituicao, name = 'detalhe_instituicao')
]
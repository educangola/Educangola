from django.contrib import admin
from cursos import views
from django.urls import path, include

urlpatterns = [
    path('Todos_cursos/', views.Todos_cursos, name="Todos_cursos" ),
    path('detalhe_curso<int:id>/', views.detalhe_curso, name = 'detalhe_curso'),
    path('incricao_curso<int:id>/', views.incricao_curso, name = 'incricao_curso'),
    path('inscricao_create<int:id>/', views.inscricao_create, name = 'inscricao_create'),
    path('ficha_inscricao<int:id>/', views.ficha_inscricao, name = 'ficha_inscricao'),
    path('conformacao_mensagem/<int:inscricao_id>/', views.conformacao_mensagem, name='conformacao_mensagem'),
    path('instrutor/', views.instrutor, name='instrutor'),

]
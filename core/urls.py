from django.urls import path, include
from django.views.i18n import set_language 
from usuarios import views as viewhome
from core import views as viewerro

urlpatterns = [
    path('home', viewhome.home, name="home"),
    path('home_cursos/', viewhome.home_cursos, name="home_cursos"),
    path('erro/', viewerro.Erro, name="erro"),
    path('set_language/', set_language, name='set_language'),  # Corrigido aqui
    path('admin/', viewerro.admin, name="admin"),
    path('i18n/', include('django.conf.urls.i18n')),
    path('sobre_nos/', viewerro.sobre_nos, name="sobre_nos"),
    path('Todos_cursos/', viewerro.Todos_cursos, name="Todos_cursos"),
    path('contactar/', viewerro.contactar, name='contactar')
]

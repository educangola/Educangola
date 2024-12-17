from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from core import views 
from core.views import Erro  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"), 
    path('Educa_Angola/', include('core.urls')), 
    path('bolsa/', include('bolsas.urls')),
    path('comentarios/', include('comentarios.urls')),
    path('cursos/', include('cursos.urls')),
    path('instituicoes/', include('instituicoes.urls')),
    path('noticias/', include('noticias.urls')),
    path('usuarios/', include('usuarios.urls'))
]

handler404 = 'core.views.Erro'



from django.urls import path, include
from django.views.i18n import set_language 
from gestoreduca import views 

urlpatterns = [
    path('login_gestor/', views.login_gestor, name='login_gestor'),
    path('codigo/', views.codigo, name = 'codigo'),
    path('home_gestoreduca/', views.home_gestoreduca, name = 'home_gestoreduca'),
    path('incricao/', views.incricao, name='incricao')
]
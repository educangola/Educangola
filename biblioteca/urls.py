from django.urls import path
from biblioteca import views

urlpatterns = [
    path('home_biblioteca/', views.home_biblioteca, name='home_biblioteca'),
]
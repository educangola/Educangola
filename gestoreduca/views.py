from django.shortcuts import render

def login_gestor(request):
    return render(request, 'login_gestor.html')

def codigo(request):
    return render(request, 'codigo.html')

def home_gestoreduca(request):
    return render(request, 'home_gestoreduca.html')

def incricao(request):
    return render(request, 'inscricao.html')
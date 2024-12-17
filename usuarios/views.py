from django.shortcuts import render
from django.http import HttpResponse  
from .models import Usuario
from django.shortcuts import redirect
from hashlib import sha256

def home(request):
    return render(request, 'home.html')


def Cadastrar_normal(request):
    status = request.GET.get('status')
    return render(request, 'cadastrar_normal.html', {'status':status}) 

def Login_normal(request):
    status = request.GET.get('status')
    return render(request, 'login_normal.html', {'status':status})

def Valida_login_normal(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha = sha256(senha.encode()).hexdigest()
    usuario = Usuario.objects.filter(email = email).filter(senha=senha)

    if len(usuario) == 0:
        return redirect('/usuarios/Login_normal?status=1')
    elif len(usuario) > 0:
        request.session['usuario'] = usuario[0].id

    return redirect('/Educa_Angola/home?status=1')


def Valida_cadastro_normal(request):
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')
    email = request.POST.get('email')

    usuario = Usuario.objects.filter(email = email)

    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/usuarios/Cadastrar_normal?status=1')

    if len(senha) < 8:
        return redirect('/usuarios/Cadastrar_normal?status=2')

    if len(usuario) > 0:
        return redirect('/usuarios/Cadastrar_normal?status=3')

    try:
        senha = sha256(senha.encode()).hexdigest()
        usuario = Usuario(nome = nome, senha = senha, email = email)
        usuario.save()
        return redirect('/usuarios/Cadastrar_normal?status=0')

    except:
        return redirect('/usuarios/Login_normal?status=4')

from django.shortcuts import render
from django.http import HttpResponse  
from .models import Usuario
from django.shortcuts import render, get_object_or_404
from cursos.models import Curso, Categoria, Instrutor, PerfilInstrutor
from django.shortcuts import redirect
from hashlib import sha256

def home(request):
    return render(request, 'home.html')



def cursos_por_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id) 
    cursos = Curso.objects.filter(categoria=categoria)
    quantidade_cursos = cursos.count()
    categoria = Categoria.objects.all()
    return render(request, 'cursos_por_categoria.html', {'categoria': categoria, 'cursos': cursos, 'categoria':categoria,'quantidade_cursos': quantidade_cursos})



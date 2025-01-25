from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils.translation import activate
from cursos.models import Curso, Categoria, Instrutor, PerfilInstrutor
from .models import Contactar



def index(request):
    cursos = Curso.objects.all()
    instrutores = Instrutor.objects.all()
    cursos_actualizados = Curso.objects.all().order_by('-data_criacao')
    categorias = Categoria.objects.all()
    return render(request, 'index.html', {'cursos': cursos, 'categorias':categorias, 'cursos_actualizados':cursos_actualizados, 'instrutores':instrutores})

def contactar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        assunto = request.POST.get('assunto')
        mensagem = request.POST.get('mensagem')


    
        contactar = Contactar(nome = nome, email = email, telefone = telefone, assunto = assunto, mensagem = mensagem)
        contactar.save()

        return redirect('/Educa_Angola/contactar?status=1')
    else:
        return redirect('/Educa_Angola/contactar?status=4')

    


def sobre_nos(request):
    return render(request, 'sobre_nos.html')

def Todos_cursos(request):
    return render(request, 'todos_cursos.html')


def Erro(request, exception):
    try:
        
        return render(request, 'erro.html', {'exception': exception}, status=404)
    except Exception as e:
        print(f"Erro ao renderizar o template: {e}")
        return render(request, 'erro.html', {'exception': str(e)}, status=500)


#-------------------Area administrativa--------------------------

def admin(request):
    return render(request, 'admin.html')



def change_language(request):
    lang_code = request.POST.get('language', 'pt-br')  # Padrão 'pt-br'
    activate(lang_code)
    return redirect(request.META.get('HTTP_REFERER'))


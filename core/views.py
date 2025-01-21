from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils.translation import activate
from cursos.models import Curso

def index(request):
    return render(request, 'index.html')


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


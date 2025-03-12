from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils.translation import activate
from cursos.models import Curso, Categoria, Instrutor, PerfilInstrutor
from .models import Contactar, Parceiro
from usuarios.models import Usuario
from django.contrib.auth.hashers import make_password
from django.urls import reverse
from biblioteca.models import Livro




def index(request):
    # Buscar os cursos em destaque
    cursos = Curso.objects.filter(destaque=True)
    cursos_actualizados = cursos.order_by('-data_criacao')

    # Dados gerais da página
    parceiros = Parceiro.objects.all()
    categorias = Categoria.objects.all()
    livros = Livro.objects.filter(destaque=True)
    quantidade_cursos = cursos.count()

    # Verifica se o usuário está logado
    usuario_id = request.session.get('usuario')
    usuario = None

    if usuario_id:
        try:
            usuario = Usuario.objects.get(id=usuario_id)
        except Usuario.DoesNotExist:
            usuario = None 

    return render(request, 'index.html', {
        'cursos': cursos,
        'cursos_actualizados': cursos.order_by('-data_criacao'),
        'livros': livros,
        'quantidade_cursos': cursos.count(),
        'quantidade_cursos': livros.count(),
        'parceiros': Parceiro.objects.all(),
        'categorias': categorias,
        'usuario': usuario,  # Enviar o nome do usuário logado (ou None se não estiver logado)
    })


def home_cursos(request):
    cursos = Curso.objects.all()
    curso_categoria_tecnologia = cursos.filter(categoria__nome__iexact="Tecnologia")
    quantidade_cursos_tecnologia = curso_categoria_tecnologia.count()
    quantidade_cursos = cursos.count()
    livros = Livro.objects.all()
    quantidade_livro = livros.count()
    cursos = Curso.objects.all()
    instrutores = Instrutor.objects.all()
    cursos_actualizados = Curso.objects.all().order_by('-data_criacao')
    categorias = Categoria.objects.all()
    return render(request, 'home_cursos.html', {'cursos': cursos, 'categorias':categorias, 'cursos_actualizados':cursos_actualizados, 'instrutores':instrutores, 'quantidade_cursos':quantidade_cursos, 'quantidade_livro':quantidade_livro, 'curso_categoria_tecnologia':curso_categoria_tecnologia, 'quantidade_cursos_tecnologia':quantidade_cursos_tecnologia})

def detalhe_livro(request, id):
    livro = get_object_or_404(Livro, id=id) 
    return render(request, 'detalhe_livro.html', {'livro': livro})

def home_biblioteca(request):
    return render(request, 'home_biblioteca.html')

def Cadastrar_normal(request):
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status':status}) 

def Login_normal(request):
    status = request.GET.get('status')
    return render(request, 'login.html', {'status':status})

def conta_aluno(request):
    usuario_id = request.session.get('usuario')

    if usuario_id:
        try:
            usuario = Usuario.objects.get(id=usuario_id) 
            return render(request, 'conta_aluno.html', {'usuario': usuario})
        except Usuario.DoesNotExist:
            pass 

    return redirect(reverse('Login_normal') + '?status=21')
    
def sair(request):
    request.session.flush()
    return redirect(reverse('index') + '?status=20')

def Valida_login_normal(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    usuario = Usuario.objects.filter(email = email).filter(senha=senha)

    if len(usuario) == 0:
        return redirect(reverse('Login_normal') + '?status=1')

    elif len(usuario) > 0:
        request.session['usuario'] = usuario[0].id

    return redirect(reverse('conta_aluno'))


def Valida_cadastro_normal(request):
    nome = request.POST.get('nome', '').strip()
    senha = request.POST.get('senha', '')
    email = request.POST.get('email', '').strip()

    if not nome or not email:
        return redirect(reverse('Cadastrar_normal') + '?status=1')  

    if len(senha) < 8:
        return redirect(reverse('Cadastrar_normal') + '?status=2')  

    if Usuario.objects.filter(email=email).exists():
        return redirect(reverse('Cadastrar_normal') + '?status=3')  

    try:
        # Criptografando a senha corretamente
        senha_criptografada = make_password(senha)

        # Criando o usuário no banco de dados
        usuario = Usuario(nome=nome, senha=senha_criptografada, email=email)
        usuario.save()

        return redirect(reverse('Cadastrar_normal') + '?status=0')  

    except Exception as e:
        print(f"Erro ao cadastrar usuário: {e}")  # Exibir erro no terminal
        return redirect(reverse('Cadastrar_normal') + '?status=4') 


def universidade(request):
    return render(request, 'universidade.html')

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
    cursos = Curso.objects.all()
    quantidade_cursos = cursos.count()
    return render(request, 'sobre_nos.html', {'cursos':cursos, 'quantidade_cursos':quantidade_cursos})

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



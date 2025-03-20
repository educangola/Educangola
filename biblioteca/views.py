from django.shortcuts import render
from biblioteca.models import Biblioteca, Livro, CategoriaLivro
from usuarios.models import Usuario






def home_biblioteca(request):
    livros_hot = Livro.objects.filter(hot=True)
    categorias = CategoriaLivro.objects.all()
    livros = Livro.objects.filter(destaque=True)
    livros_destaques = Livro.objects.filter(destaque=True)
    # Verifica se o usuário está logado
    usuario_id = request.session.get('usuario')
    usuario = None

    if usuario_id:
        try:
            usuario = Usuario.objects.get(id=usuario_id)
        except Usuario.DoesNotExist:
            usuario = None 
    return render(request, 'home_biblioteca.html', {'livros_hot':livros_hot,'categorias':categorias, 'livros_destaques':livros_destaques, 'livros':livros, 'usuario':usuario})



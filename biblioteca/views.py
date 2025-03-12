from django.shortcuts import render
from biblioteca.models import Biblioteca, Livro, CategoriaLivro




def home_biblioteca(request):
    livros_hot = Livro.objects.filter(hot=True)
    categorias = CategoriaLivro.objects.all()
    livros = Livro.objects.filter(destaque=True)
    livros_destaques = Livro.objects.filter(destaque=True)
    return render(request, 'home_biblioteca.html', {'livros_hot':livros_hot,'categorias':categorias, 'livros_destaques':livros_destaques, 'livros':livros})



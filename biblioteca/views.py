from django.shortcuts import render
from biblioteca.models import Biblioteca, Livro




def home_biblioteca(request):
    livros_hot = Livro.objects.filter(hot=True)
    return render(request, 'home_biblioteca.html', {'livros_hot':livros_hot})

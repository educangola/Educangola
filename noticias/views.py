from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from noticias.models import Noticia, Categoria


def recente_news(request):
    # Obtendo as 5 últimas notícias ordenadas por data de publicação
    recente_news = Noticia.objects.all().order_by('-data_publicacao')[:5]
    return render(request, 'noticia_recentes.html', {'recente_news': recente_news})


def noticia(request):
    categorias = Categoria.objects.all()
    noticias = Noticia.objects.all().order_by('-data_publicacao')[:10]
    return render(request, 'noticia.html', {'noticia': noticias, 'categorias': categorias})


def noticia_por_categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)  
    noticias = Noticia.objects.filter(categoria=categoria).order_by('-data_publicacao') 
    return render(request, 'categoria_notica.html', {'noticia': noticias, 'categoria_obj': categoria})


def noticia_detalhe(request, id):
    noticia = get_object_or_404(Noticia, id=id)
    return render(request, 'noticia_detalhe.html', {'noticia': noticia})


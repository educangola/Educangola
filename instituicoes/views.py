from django.shortcuts import render
from .models import Instituicao



def Instituicao(request):
    escolas = Instituicao.get.all()
    return render(request, 'escolas.html')


def detalhe_instituicao(request, id):
    escola = get_object_or_404(Instituicao, id=id) 
    return render(request, 'detalhe_instituicao.html',{'escola':escola})
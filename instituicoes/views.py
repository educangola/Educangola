from django.shortcuts import render
from .models import Instituicao



def Instituicao(request):
    escolas = Instituicao.get.all()
    return render(request, 'escolas.html')



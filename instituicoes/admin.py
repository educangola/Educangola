from django.contrib import admin
from .models import Instituicao, InstituicaoImagem, CentrosImagem, Centros

admin.site.register(Instituicao)
admin.site.register(InstituicaoImagem)
admin.site.register(Centros)
admin.site.register(CentrosImagem)

from django.contrib import admin
from .models import Curso, Categoria, Inscricao, Instrutor, PerfilInstrutor

admin.site.register(Curso)
admin.site.register(Categoria)
admin.site.register(Inscricao)
admin.site.register(Instrutor)
admin.site.register(PerfilInstrutor)



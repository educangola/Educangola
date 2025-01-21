from django.contrib import admin
from .models import Forum, Postagem, Comentario

@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'usuario_criador', 'data_criacao')
    search_fields = ('titulo', 'descricao')
    list_filter = ('data_criacao', 'usuario_criador')
    ordering = ('-data_criacao',)

@admin.register(Postagem)
class PostagemAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'forum', 'usuario', 'data_criacao', 'data_atualizacao')
    search_fields = ('titulo', 'conteudo')
    list_filter = ('data_criacao', 'forum', 'usuario')
    ordering = ('-data_criacao',)

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('postagem', 'usuario', 'data_criacao')
    search_fields = ('conteudo',)
    list_filter = ('data_criacao', 'usuario')
    ordering = ('-data_criacao',)

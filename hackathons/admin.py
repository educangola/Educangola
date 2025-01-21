from django.contrib import admin
from .models import Hackathon, Participante, Equipe, Desafio, Submissao, Avaliacao
from django.utils.html import format_html

# Personalizando o modelo Hackathon no Admin
@admin.register(Hackathon)
class HackathonAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'data_inicio', 'data_fim', 'ativo', 'criador')
    search_fields = ('nome', 'descricao')
    list_filter = ('ativo', 'criador')

    class Media:
        js = ('https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free/js/all.js',)

# Personalizando o modelo Participante no Admin
@admin.register(Participante)
class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'hackathon', 'inscricao_data')
    search_fields = ('usuario__nome', 'hackathon__nome')

# Personalizando o modelo Equipe no Admin
@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'hackathon', 'descricao', 'data_criacao')
    search_fields = ('nome', 'hackathon__nome')

# Personalizando o modelo Desafio no Admin
@admin.register(Desafio)
class DesafioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'data_inicio', 'data_fim', 'hackathon')
    search_fields = ('titulo', 'descricao')

# Personalizando o modelo Submissao no Admin
@admin.register(Submissao)
class SubmissaoAdmin(admin.ModelAdmin):
    list_display = ('equipe', 'desafio', 'data_submissao', 'arquivo')
    search_fields = ('equipe__nome', 'desafio__titulo')

# Personalizando o modelo Avaliacao no Admin
@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('juiz', 'submissao', 'nota', 'comentario')
    search_fields = ('juiz__nome', 'submissao__equipe__nome')

# Personalizando o painel Admin do Hackathon para adicionar ícones
class HackathonAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'data_inicio', 'data_fim', 'ativo', 'criador')
    search_fields = ('nome', 'descricao')
    list_filter = ('ativo', 'criador')

    # Adicionando ícones ao painel de admin usando Jazzmin
    jazzmin_list_icons = {
        'Hackathon': 'fas fa-trophy',  # Usando o ícone de troféu para o Hackathon
        'Participante': 'fas fa-user',  # Ícone de usuário para Participante
        'Equipe': 'fas fa-users',  # Ícone de usuários para Equipe
        'Desafio': 'fas fa-chalkboard',  # Ícone de quadro negro para Desafio
        'Submissao': 'fas fa-upload',  # Ícone de upload para Submissão
        'Avaliacao': 'fas fa-star',  # Ícone de estrela para Avaliação
    }


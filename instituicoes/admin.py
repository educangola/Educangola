from django.contrib import admin
from .models import Instituicao, Categoria, SeguirInstituicao, Curso, Inscricao, PerfilInstituicao, Postagem, DadosUpload, Status

# Personalizando a interface de cada modelo

@admin.register(Instituicao)
class InstituicaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'status_relacionado')  # Modificado para usar método customizado
    list_filter = ('perfil__status',)  # Filtra pelo status do PerfilInstituicao relacionado
    search_fields = ('nome', 'email')
    icon = 'fas fa-university'

    # Método para acessar o status relacionado do PerfilInstituicao
    def status_relacionado(self, obj):
        return obj.perfil.status.status  # Acessando o campo status do PerfilInstituicao
    status_relacionado.short_description = 'Status'

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    icon = 'fas fa-tags'

@admin.register(SeguirInstituicao)
class SeguirInstituicaoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'instituicao', 'data_seguindo')
    icon = 'fas fa-user-plus'

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'numero_vagas', 'instituicoes_nomes')
    list_filter = ('categoria',)  # Filtro de categoria
    search_fields = ('nome',)  # Pesquisa por nome de curso
    icon = 'fas fa-book'

    def instituicoes_nomes(self, obj):
        return ", ".join([instituicao.nome for instituicao in obj.instituicoes.all()])
    instituicoes_nomes.short_description = 'Instituições'

@admin.register(Inscricao)
class InscricaoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'curso', 'data_inscricao')
    icon = 'fas fa-pencil-alt'

@admin.register(PerfilInstituicao)
class PerfilInstituicaoAdmin(admin.ModelAdmin):
    list_display = ('login', 'tipo', 'cidade')
    icon = 'fas fa-id-badge'

@admin.register(Postagem)
class PostagemAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'instituicao', 'data_criacao')
    icon = 'fas fa-newspaper'

@admin.register(DadosUpload)
class DadosUploadAdmin(admin.ModelAdmin):
    list_display = ('perfil_instituicao', 'arquivo', 'descricao')
    icon = 'fas fa-upload'


admin.site.register(Status)
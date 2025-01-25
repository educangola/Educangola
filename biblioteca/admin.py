from django.contrib import admin
from .models import CategoriaBiblioteca, Biblioteca, Livro, UsuarioBiblioteca, Emprestimo, Tese, ConsultoriaTCC, EmprestimoTese, CategoriaLivro

# Registra os modelos no Django Admin com os ícones configurados no Jazzmin

class CategoriaBibliotecaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

admin.site.register(CategoriaLivro)

class BibliotecaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'endereco', 'cidade', 'telefone', 'data_criacao', 'categoria', 'site')
    search_fields = ('nome', 'email', 'cidade')
    list_filter = ('categoria',)

class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'editora', 'ano_publicacao', 'isbn', 'biblioteca', 'disponivel')
    search_fields = ('titulo', 'autor', 'isbn')
    list_filter = ('biblioteca', 'disponivel')

class UsuarioBibliotecaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'biblioteca')
    search_fields = ('nome', 'email')
    list_filter = ('biblioteca',)

class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'livro', 'data_emprestimo', 'data_devolucao', 'devolvido')
    search_fields = ('usuario__nome', 'livro__titulo')
    list_filter = ('devolvido',)

class TeseAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'orientador', 'ano_publicacao', 'biblioteca')
    search_fields = ('titulo', 'autor', 'orientador', 'ano_publicacao')
    list_filter = ('biblioteca',)

class ConsultoriaTCCAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'assunto', 'status', 'data_solicitacao')
    search_fields = ('usuario__nome', 'assunto', 'status')
    list_filter = ('status',)

class EmprestimoTeseAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'tese', 'data_emprestimo', 'data_devolucao', 'devolvido')
    search_fields = ('usuario__nome', 'tese__titulo')
    list_filter = ('devolvido',)

# Registro dos modelos com os ícones configurados via Jazzmin
admin.site.register(CategoriaBiblioteca, CategoriaBibliotecaAdmin)
admin.site.register(Biblioteca, BibliotecaAdmin)
admin.site.register(Livro, LivroAdmin)
admin.site.register(UsuarioBiblioteca, UsuarioBibliotecaAdmin)
admin.site.register(Emprestimo, EmprestimoAdmin)
admin.site.register(Tese, TeseAdmin)
admin.site.register(ConsultoriaTCC, ConsultoriaTCCAdmin)
admin.site.register(EmprestimoTese, EmprestimoTeseAdmin)

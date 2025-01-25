from django.contrib import admin
from .models import Bolsa

@admin.register(Bolsa)
class BolsaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'instituicao', 'curso', 'data_inicio', 'data_fim', 'ativo')
    search_fields = ('nome', 'instituicao__nome', 'curso__nome')
    list_filter = ('instituicao', 'curso', 'ativo')
    date_hierarchy = 'data_inicio'

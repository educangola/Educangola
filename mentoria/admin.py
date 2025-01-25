from django.contrib import admin
from .models import Mentor, Mentee, SessaoMentoria, Feedback, Agendamento

# Registra os modelos no admin
@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'especialidade', 'telefone', 'data_criacao')
    search_fields = ('nome', 'especialidade', 'email')

@admin.register(Mentee)
class MenteeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'data_criacao')
    search_fields = ('nome', 'email')

@admin.register(SessaoMentoria)
class SessaoMentoriaAdmin(admin.ModelAdmin):
    list_display = ('mentor', 'mentee', 'data_sessao', 'duracao', 'status')
    list_filter = ('status', 'data_sessao')
    search_fields = ('mentor__nome', 'mentee__nome', 'assunto')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('sessao', 'mentee', 'nota', 'comentario')
    search_fields = ('sessao__mentor__nome', 'mentee__nome')

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('mentor', 'mentee', 'data_agendada', 'status')
    list_filter = ('status',)
    search_fields = ('mentor__nome', 'mentee__nome')

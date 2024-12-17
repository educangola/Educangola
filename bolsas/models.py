# bolsas/models.py
from django.db import models
from instituicoes.models import Instituicao
from cursos.models import Curso

class Bolsa(models.Model):
    nome = models.CharField(max_length=255)
    instituicao = models.ForeignKey(Instituicao, related_name='bolsas', on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, related_name='bolsas', on_delete=models.CASCADE, blank=True, null=True)
    descricao = models.TextField()
    requisitos = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Valor da bolsa (opcional)
    link_inscricao = models.URLField(max_length=500, blank=True, null=True)  # Link para a inscrição
    ativo = models.BooleanField(default=True)  # Indica se a bolsa está ativa

    def __str__(self):
        return self.nome

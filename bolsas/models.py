from django.db import models
from instituicoes.models import Instituicao
from cursos.models import Curso

class Bolsa(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome da Bolsa")
    instituicao = models.ForeignKey(
        Instituicao,
        related_name='bolsas',
        on_delete=models.DO_NOTHING,
        verbose_name="Instituição"
    )
    curso = models.ForeignKey(
        Curso,
        related_name='bolsas',
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        verbose_name="Curso"
    )
    descricao = models.TextField(verbose_name="Descrição")
    requisitos = models.TextField(verbose_name="Requisitos")
    data_inicio = models.DateField(verbose_name="Data de Início")
    data_fim = models.DateField(verbose_name="Data de Fim")
    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Valor da Bolsa"
    )
    link_inscricao = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name="Link de Inscrição"
    )
    ativo = models.BooleanField(default=True, verbose_name="Ativo")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Bolsa"
        verbose_name_plural = "Bolsas"
        ordering = ['nome']

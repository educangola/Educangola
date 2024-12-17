from django.db import models
from instituicoes.models import Instituicao

class Curso(models.Model):
    instituicao = models.ForeignKey(Instituicao, related_name='cursos', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    duracao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    nivel = models.CharField(max_length=100, choices=[('Básico', 'Básico'), ('Intermediário', 'Intermediário'), ('Avançado', 'Avançado')])
    modalidade = models.CharField(max_length=100, choices=[('Presencial', 'Presencial'), ('Online', 'Online')])
    data_inicio = models.DateField()
    data_fim = models.DateField()

    def __str__(self):
        return self.nome

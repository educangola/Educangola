from django.db import models
from usuarios.models import Usuario
from cursos.models import Curso


class Inscricao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    data_inscricao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('pendente', 'Pendente'), ('confirmado', 'Confirmado')])
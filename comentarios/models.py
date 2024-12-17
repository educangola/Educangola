from django.db import models
from usuarios.models import Usuario
from instituicoes.models import Instituicao
from cursos.models import Curso

class ComentarioInstituicao(models.Model):
    usuario = models.ForeignKey(Usuario, related_name='comentarios_instituicao', on_delete=models.CASCADE)
    instituicao = models.ForeignKey(Instituicao, related_name='comentarios_instituicao', on_delete=models.CASCADE)
    texto = models.TextField()
    data_comentario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário de {self.usuario.username} sobre {self.instituicao.nome}"

class ComentarioCurso(models.Model):
    usuario = models.ForeignKey(Usuario, related_name='comentarios_curso', on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, related_name='comentarios_curso', on_delete=models.CASCADE)
    texto = models.TextField()
    data_comentario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário de {self.usuario.username} sobre o curso {self.curso.nome}"

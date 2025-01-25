from django.db import models

class Contactar(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.IntegerField()
    assunto = models.CharField(max_length=50)
    mensagem = models.TextField()

    def __str__(self):
        return self.nome
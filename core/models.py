from django.db import models

class Contactar(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.IntegerField()
    assunto = models.CharField(max_length=50)
    mensagem = models.TextField()

    def __str__(self):
        return self.nome
    
class Parceiro(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='parceiros/', blank=True, null=True)
    
    
    def __str__(self):
        return self.nome
from django.db import models

class Instituicao(models.Model):
    nome = models.CharField(max_length=255)
    tipo = models.CharField(max_length=100, choices=[('Escola', 'Escola'), ('Centro de Formação', 'Centro de Formação')])
    descricao = models.TextField()
    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    contato = models.CharField(max_length=100)
    email = models.EmailField()
    site = models.URLField(blank=True, null=True)
    data_fundacao = models.DateField()
    logo = models.ImageField(upload_to='instituicoes/logos/', blank=True, null=True)

    def __str__(self):
        return self.nome

class InstituicaoImagem(models.Model):
    instituicao = models.ForeignKey(Instituicao, related_name='imagens', on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='instituicoes/imagens/')
    descricao = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Imagem de {self.instituicao.nome}"


class Centros(models.Model):
    nome = models.CharField(max_length=255)
    tipo = models.CharField(max_length=100, choices=[('Escola', 'Escola'), ('Centro de Formação', 'Centro de Formação')])
    descricao = models.TextField()
    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    contato = models.CharField(max_length=100)
    email = models.EmailField()
    site = models.URLField(blank=True, null=True)
    data_fundacao = models.DateField()
    logo = models.ImageField(upload_to='centros/logos/', blank=True, null=True)

    def __str__(self):
        return self.nome

class CentrosImagem(models.Model):
    centro = models.ForeignKey(Centros, related_name='imagens', on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='Centros/imagens/')
    descricao = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Imagem de {self.centros.nome}"

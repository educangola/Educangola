from django.db import models

class Noticia(models.Model):
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    autor = models.CharField(max_length=255)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    categoria = models.CharField(max_length=100, choices=[('Bolsas de Estudo', 'Bolsas de Estudo'), ('Eventos', 'Eventos'), ('Notícias Educacionais', 'Notícias Educacionais')])
    imagem = models.ImageField(upload_to='noticias/', blank=True, null=True)

    def __str__(self):
        return self.titulo

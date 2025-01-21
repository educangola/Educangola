from usuarios.models import Usuario 
from django.db import models

class Forum(models.Model):
    titulo = models.CharField(max_length=255)  
    descricao = models.TextField() 
    data_criacao = models.DateTimeField(auto_now_add=True)  
    usuario_criador = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, related_name='forums_criados')  
    imagem = models.ImageField(upload_to='foruns/', blank=True, null=True)  
    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Fórum"
        verbose_name_plural = "Fóruns"

class Postagem(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.DO_NOTHING, related_name='postagens')  
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, related_name='postagens')
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()  
    data_criacao = models.DateTimeField(auto_now_add=True) 
    data_atualizacao = models.DateTimeField(auto_now=True)
    imagem = models.ImageField(upload_to='postagens/', blank=True, null=True)  # 
    
    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Postagem"
        verbose_name_plural = "Postagens"

class Comentario(models.Model):
    postagem = models.ForeignKey(Postagem, on_delete=models.DO_NOTHING, related_name='comentarios') 
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, related_name='comentarios')
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Comentário de {self.usuario.nome} na postagem {self.postagem.titulo}'

    class Meta:
        verbose_name = "Comentário"
        verbose_name_plural = "Comentários"

from django.db import models
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


# models.py

from django.db import models
from django.utils.text import slugify

class Tag(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name="Nome da Tag")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome


class Noticia(models.Model):
    # Título da notícia
    titulo = models.CharField(
        max_length=255,
        verbose_name="Título da Notícia"  # Nome amigável para o campo
    )
    
    # Resumo da notícia, campo opcional
    resumo = models.CharField(
        max_length=500, 
        blank=True, 
        null=True,
        verbose_name="Resumo da Notícia"
    )
    
    # Conteúdo completo da notícia
    conteudo = models.TextField(
        verbose_name="Conteúdo"
    )
    
    # Autor da notícia
    autor = models.CharField(
        max_length=255,
        verbose_name="Autor"
    )
    
    # E-mail do autor (opcional)
    autor_email = models.EmailField(
        blank=True, 
        null=True,
        verbose_name="E-mail do Autor"
    )
    
    # Data de publicação da notícia
    data_publicacao = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Data de Publicação"
    )
    
    # Data de última atualização da notícia
    data_atualizacao = models.DateTimeField(
        auto_now=True, 
        verbose_name="Data de Atualização"
    )
    
    # Relacionamento com Categoria
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.DO_NOTHING, 
        related_name='noticias',
        verbose_name="Categoria"
    )
    
    # Imagem principal associada à notícia (opcional)
    imagem = models.ImageField(
        upload_to='noticias/', 
        blank=True, 
        null=True,
        verbose_name="Imagem Principal"
    )
    
    # Imagem alternativa, caso a principal não seja exibida ou para dispositivos móveis (opcional)
    imagem_alternativa = models.ImageField(
        upload_to='noticias/', 
        blank=True, 
        null=True,
        verbose_name="Imagem Alternativa"
    )
    
    # Fonte da notícia (URL) - caso seja relevante
    fonte = models.URLField(
        blank=True, 
        null=True,
        verbose_name="Fonte"
    )
    
    # Tags associadas à notícia, para organização e busca
    tags = models.ManyToManyField(
        'Tag', 
        blank=True,
        verbose_name="Tags"
    )
    
    # URL de um vídeo relacionado à notícia (opcional)
    video_url = models.URLField(
        blank=True, 
        null=True,
        verbose_name="URL do Vídeo"
    )
    
    # Localização associada à notícia (exemplo: local de um evento)
    localizacao = models.CharField(
        max_length=255, 
        blank=True, 
        null=True,
        verbose_name="Localização"
    )
    
    # Campo para destacar a notícia em algum lugar (exemplo: para exibição em destaque)
    destaque = models.BooleanField(
        default=False,
        verbose_name="Destacar Notícia"
    )
    
    # Status da notícia (Publicado, Em revisão, Arquivado)
    status = models.CharField(
        max_length=20, 
        choices=[
            ('Publicado', 'Publicado'),
            ('Em revisão', 'Em revisão'),
            ('Arquivado', 'Arquivado')
        ], 
        default='Publicado',
        verbose_name="Status"
    )
    
    # Notícia relacionada a outras (exemplo: para exibir notícias semelhantes)
    noticias_relacionadas = models.ManyToManyField(
        'self', 
        blank=True,
        verbose_name="Notícias Relacionadas"
    )
    
    # Leitura recomendada, para sugerir outras notícias relevantes
    leitura_recomendada = models.ManyToManyField(
        'self', 
        blank=True,
        verbose_name="Leitura Recomendada"
    )

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Notícia"
        verbose_name_plural = "Notícias"


class Post(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    conteudo = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name='posts')
    data_publicacao = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    publicado = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.CharField(max_length=100)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    aprovado = models.BooleanField(default=False)

    def __str__(self):
        return f'Comentário de {self.autor} em {self.post.titulo}'


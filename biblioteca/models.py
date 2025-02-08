from django.db import models

class CategoriaBiblioteca(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Categoria da Biblioteca"
        verbose_name_plural = "Categorias das Bibliotecas"

class PerfilBiblioteca(models.Model):
    biblioteca = models.OneToOneField('Biblioteca', on_delete=models.CASCADE)
    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    data_criacao = models.DateField(auto_now_add=True)
    categoria = models.ForeignKey(CategoriaBiblioteca, on_delete=models.SET_NULL, null=True)
    site = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='bibliotecas/logos/', blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.biblioteca.nome}"

    class Meta:
        verbose_name = "Perfil da Biblioteca"
        verbose_name_plural = "Perfis das Bibliotecas"

class Biblioteca(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Biblioteca"
        verbose_name_plural = "Bibliotecas"


class CategoriaLivro(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Categoria de Livro"
        verbose_name_plural = "Categorias de Livros"


class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    editora = models.CharField(max_length=100)
    ano_publicacao = models.PositiveIntegerField()
    isbn = models.CharField(max_length=13, unique=True, blank=True)
    biblioteca = models.ForeignKey(Biblioteca, on_delete=models.DO_NOTHING, related_name='livros')
    disponivel = models.BooleanField(default=True)
    categoria = models.ForeignKey(CategoriaLivro, on_delete=models.DO_NOTHING, null=True)
    imagem = models.ImageField(upload_to='livros/imagens/', blank=True, null=True)
    hot = models.BooleanField(default=False)
    
    # Novos campos adicionados
    tags = models.CharField(max_length=255, blank=True)  # Tags
    formato = models.CharField(max_length=50)  # Formato
    total_paginas = models.PositiveIntegerField()  # Total de páginas
    idioma = models.CharField(max_length=50)  # Idioma
    ano_publicacao = models.PositiveIntegerField()  # Ano de publicação
    secao = models.CharField(max_length=100)  # Século (ex: United States, etc.)
    
    def __str__(self):
        return f"{self.titulo} - {self.autor}"

    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"



class UsuarioBiblioteca(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)
    biblioteca = models.ForeignKey(Biblioteca, on_delete=models.DO_NOTHING, related_name='usuarios')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Usuário da Biblioteca"
        verbose_name_plural = "Usuários da Biblioteca"


class Emprestimo(models.Model):
    usuario = models.ForeignKey(UsuarioBiblioteca, on_delete=models.DO_NOTHING)
    livro = models.ForeignKey(Livro, on_delete=models.DO_NOTHING)
    data_emprestimo = models.DateTimeField(auto_now_add=True)
    data_devolucao = models.DateField()
    devolvido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.usuario.nome} emprestou {self.livro.titulo}"

    class Meta:
        verbose_name = "Empréstimo"
        verbose_name_plural = "Empréstimos"


class Tese(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    orientador = models.CharField(max_length=255)
    ano_publicacao = models.PositiveIntegerField()
    resumo = models.TextField()
    biblioteca = models.ForeignKey(Biblioteca, on_delete=models.DO_NOTHING, related_name='teses')

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Tese"
        verbose_name_plural = "Teses"


class ConsultoriaTCC(models.Model):
    usuario = models.ForeignKey(UsuarioBiblioteca, on_delete=models.DO_NOTHING, related_name='consultorias')
    assunto = models.CharField(max_length=255)
    descricao = models.TextField()
    data_solicitacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('pendente', 'Pendente'), ('concluida', 'Concluída')], default='pendente')

    def __str__(self):
        return f"Consulta TCC de {self.usuario.nome}"

    class Meta:
        verbose_name = "Consultoria de TCC"
        verbose_name_plural = "Consultorias de TCC"


class EmprestimoTese(models.Model):
    usuario = models.ForeignKey(UsuarioBiblioteca, on_delete=models.DO_NOTHING)
    tese = models.ForeignKey(Tese, on_delete=models.DO_NOTHING)
    data_emprestimo = models.DateTimeField(auto_now_add=True)
    data_devolucao = models.DateField()
    devolvido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.usuario.nome} emprestou a tese {self.tese.titulo}"

    class Meta:
        verbose_name = "Empréstimo de Tese"
        verbose_name_plural = "Empréstimos de Teses"

from django.db import models
from usuarios.models import Usuario


class Categoria(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Instituicao(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
    
class Blog(models.Model):
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, related_name='blogs')
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo


class Noticia(models.Model):
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, related_name='noticias')
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Contacto(models.Model):
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, related_name='contactos')
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.CharField(max_length=20, null=True, blank=True)
    mensagem = models.TextField()

    def __str__(self):
        return f"Contacto de {self.nome}"


class SobreNos(models.Model):
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, related_name='sobre_nos')
    descricao = models.TextField()
    missao = models.TextField()
    visao = models.TextField()

    def __str__(self):
        return f"Sobre a {self.instituicao.nome}"

class SeguirInstituicao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, related_name="instituicoes_seguidas")
    instituicao = models.ForeignKey(Instituicao, on_delete=models.DO_NOTHING, related_name="seguidores")
    data_seguindo = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.nome} segue {self.instituicao.nome}"


class Curso(models.Model):
    imagem = models.ImageField(upload_to='instituicoes/logos/', blank=True, null=True)
    nome = models.CharField(max_length=100)
    instituicoes = models.ManyToManyField('Instituicao', related_name="cursos_oferecidos")
    categoria = models.ForeignKey('Categoria', on_delete=models.DO_NOTHING)
    descricao = models.TextField()
    numero_vagas = models.PositiveIntegerField()

    def __str__(self):
        return self.nome

    def vagas_disponiveis(self):
        return self.numero_vagas




class Status(models.Model):
    status = models.CharField(max_length=100)


class PerfilInstituicao(models.Model):
    login = models.OneToOneField(Instituicao, on_delete=models.DO_NOTHING, related_name='perfil')
    tipo = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    descricao = models.TextField()
    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    contato = models.CharField(max_length=100)
    email = models.EmailField()
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING)
    site = models.URLField(blank=True, null=True)
    data_fundacao = models.DateField()
    logo = models.ImageField(upload_to='instituicoes/logos/', blank=True, null=True)

    def __str__(self):
        return self.login.nome


class Postagem(models.Model):
    instituicao = models.ForeignKey(Instituicao, on_delete=models.DO_NOTHING, related_name='postagens')
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class DadosUpload(models.Model):
    perfil_instituicao = models.ForeignKey(PerfilInstituicao, on_delete=models.DO_NOTHING)
    arquivo = models.FileField(upload_to='uploads/', blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Upload de {self.perfil_instituicao.login.nome}"

from django.db import models

class Habilidade(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome

# Modelo PerfilUsuario
class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name="perfil")
    
    bio = models.TextField(null=True, blank=True) 
    foto_perfil = models.ImageField(upload_to='perfil/', null=True, blank=True) 
    telefone = models.CharField(max_length=15, null=True, blank=True) 
    endereco = models.CharField(max_length=255, null=True, blank=True) 
    habilidades = models.ManyToManyField(Habilidade, blank=True) 
    data_nascimento = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Perfil de {self.usuario.nome}"

    class Meta:
        verbose_name = "Perfil do Usuário"
        verbose_name_plural = "Perfis de Usuários"


class TopicoEstudo(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


# Model para representar o Grupo de Estudo
class GrupoEstudo(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    membros = models.ManyToManyField('Usuario', related_name='grupos')  # Usando o modelo Usuario existente
    data_criacao = models.DateTimeField(auto_now_add=True)
    topicos = models.ManyToManyField(TopicoEstudo, related_name='grupos', blank=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


# Model para representar Sessões de Estudo
class SessaoEstudo(models.Model):
    grupo = models.ForeignKey(GrupoEstudo, on_delete=models.CASCADE, related_name='sessoes')
    data_sessao = models.DateTimeField()
    local = models.CharField(max_length=255)
    topico = models.ForeignKey(TopicoEstudo, on_delete=models.SET_NULL, null=True, blank=True)
    duracao = models.PositiveIntegerField()  # Duração da sessão em minutos
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Sessão de Estudo - {self.grupo.nome} - {self.data_sessao}"


# Model para representar Materiais de Estudo compartilhados no grupo
class MaterialEstudo(models.Model):
    grupo = models.ForeignKey(GrupoEstudo, on_delete=models.CASCADE, related_name='materiais')
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    arquivo = models.FileField(upload_to='materiais_estudo/')
    data_upload = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


# Model para representar Feedback de Sessões de Estudo
class FeedbackSessao(models.Model):
    sessao = models.ForeignKey(SessaoEstudo, on_delete=models.CASCADE, related_name='feedbacks')
    membro = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='feedbacks')  # Usando o modelo Usuario
    nota = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comentario = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Feedback de {self.membro.username} para a sessão de estudo"

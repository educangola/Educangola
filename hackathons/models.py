from django.db import models
from usuarios.models import Usuario  # Importando o modelo Usuario da sua app 'usuarios'

# Modelo para representar um Hackathon
class Hackathon(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    local = models.CharField(max_length=255, blank=True, null=True)
    ativo = models.BooleanField(default=True)
    criador = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, null=True, related_name='hackathons')

    def __str__(self):
        return self.nome


# Modelo para representar os Participantes no Hackathon
class Participante(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)  # Usando o modelo Usuario
    hackathon = models.ForeignKey(Hackathon, on_delete=models.DO_NOTHING, related_name='participantes')
    equipe = models.ForeignKey('Equipe', on_delete=models.DO_NOTHING, null=True, blank=True)
    inscricao_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.nome} - {self.hackathon.nome}"


# Modelo para representar uma Equipe no Hackathon
class Equipe(models.Model):
    nome = models.CharField(max_length=255)
    hackathon = models.ForeignKey(Hackathon, on_delete=models.DO_NOTHING, related_name='equipes')
    membros = models.ManyToManyField(Participante, related_name='equipes')
    descricao = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


# Modelo para representar um Desafio no Hackathon
class Desafio(models.Model):
    hackathon = models.ForeignKey(Hackathon, on_delete=models.DO_NOTHING, related_name='desafios')
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()

    def __str__(self):
        return self.titulo


# Modelo para representar a Submissão de uma equipe a um Desafio
class Submissao(models.Model):
    desafio = models.ForeignKey(Desafio, on_delete=models.DO_NOTHING, related_name='submissoes')
    equipe = models.ForeignKey(Equipe, on_delete=models.DO_NOTHING, related_name='submissoes')
    data_submissao = models.DateTimeField(auto_now_add=True)
    arquivo = models.FileField(upload_to='submissoes/', blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Submissão de {self.equipe.nome} - Desafio: {self.desafio.titulo}"


# Modelo para representar a Avaliação das Submissões (Feedback dos juízes)
class Avaliacao(models.Model):
    submissao = models.ForeignKey(Submissao, on_delete=models.DO_NOTHING, related_name='avaliacoes')
    juiz = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, null=True, related_name='avaliacoes')  # Usando o modelo Usuario
    nota = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 11)])  # Avaliação de 1 a 10
    comentario = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Avaliação de {self.juiz.nome} - Submissão: {self.submissao.equipe.nome}"

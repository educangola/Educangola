from django.db import models
from instituicoes.models import Instituicao
from decimal import Decimal


class Categoria(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome



class Curso(models.Model):
    instituicao = models.ForeignKey(Instituicao, related_name='cursos', on_delete=models.DO_NOTHING)
    categoria = models.ForeignKey(Categoria, related_name='cursos', on_delete=models.CASCADE) 
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    duracao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=15, decimal_places=3, null=True, blank=True)
    nivel = models.CharField(max_length=100, choices=[('Básico', 'Básico'), ('Intermediário', 'Intermediário'), ('Avançado', 'Avançado')])
    modalidade = models.CharField(max_length=100, choices=[('Presencial', 'Presencial'), ('Online', 'Online')])
    data_inicio = models.DateField()
    data_fim = models.DateField()
    imagem = models.ImageField(upload_to='imagens_cursos/', null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True, null=True, blank=True)  # Novo campo

    def __str__(self):
        return self.nome

    @property
    def imposto_estadual(self):
        """
        Calcula o imposto estadual (14%) com base no preço do curso.
        """
        if self.preco:
            return round(self.preco * Decimal('0.14'), 3)  # Converte 0.14 para Decimal
        return Decimal('0.0')

    @property
    def preco_com_desconto(self):
        """
        Calcula o preço com desconto (10% de desconto por exemplo).
        """
        if self.preco:
            desconto = self.preco * Decimal('0.10')  # 10% de desconto
            return self.preco - desconto
        return Decimal('0.0')

    @property
    def preco_final(self):
        """
        Calcula o preço final considerando o imposto estadual e o desconto.
        """
        preco_com_imposto = self.preco_com_desconto + self.imposto_estadual
        return round(preco_com_imposto, 3)



class Inscricao(models.Model):
    curso = models.ForeignKey(Curso, related_name='inscricoes', on_delete=models.CASCADE)  # 
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.CharField(max_length=20, null=True, blank=True)  
    data_inscricao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=50,
        choices=[
            ('Pendente', 'Pendente'),
            ('Confirmada', 'Confirmada'),
            ('Cancelada', 'Cancelada')
        ],
        default='Pendente'
    )
    observacoes = models.TextField(null=True, blank=True)  # Campo para observações adicionais

    # Novos campos
    data_nascimento = models.DateField(null=True, blank=True)  # Data de nascimento
    cidade = models.CharField(max_length=100, null=True, blank=True)  # Cidade
    bairro = models.CharField(max_length=100, null=True, blank=True)  # Bairro
    pais = models.CharField(max_length=100, null=True, blank=True)  # País
    codigo_postal = models.CharField(max_length=10, null=True, blank=True)  # Código Postal
    endereco = models.TextField(null=True, blank=True)  # Endereço
    genero = models.CharField(
        max_length=10,
        choices=[
            ('Masculino', 'Masculino'),
            ('Feminino', 'Feminino'),
            ('Outro', 'Outro')
        ],
        null=True, blank=True  # Gênero pode ser opcional
    )

    def __str__(self):
        return f"{self.nome} - {self.curso.nome}"



class Instrutor(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)  # Senha (use hashing no mundo real)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)  # Associação com o centro de formação

    def __str__(self):
        return self.nome

    def obter_media_avaliacao(self):
        return self.avaliacao

class PerfilInstrutor(models.Model):
    instrutor = models.OneToOneField(Instrutor, on_delete=models.CASCADE)  # Relacionamento com Instrutor
    biografia = models.TextField()
    titulo = models.CharField(max_length=255)
    imagem = models.ImageField(upload_to='instrutores/')
    cursos = models.IntegerField()
    estudantes = models.IntegerField()
    avaliacao = models.FloatField()
    especializacoes = models.TextField()
    contato = models.CharField(max_length=255)

    def __str__(self):
        return f'Perfil de {self.instrutor.nome}'

    def exibir_perfil_completo(self):
        return {
            'Nome': self.instrutor.nome,
            'Email': self.instrutor.email,
            'Título': self.instrutor.titulo,
            'Cursos': self.instrutor.cursos,
            'Estudantes': self.instrutor.estudantes,
            'Avaliação': self.instrutor.obter_media_avaliacao(),
            'Biografia': self.biografia,
            'Especializações': self.especializacoes,
            'Contato': self.contato,
        }

    

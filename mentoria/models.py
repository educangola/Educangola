from django.db import models

# Model para representar um Mentor
class Mentor(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    especialidade = models.CharField(max_length=255)  
    bio = models.TextField() 
    telefone = models.CharField(max_length=20, blank=True, null=True)
    data_criacao = models.DateField(auto_now_add=True)  
    def __str__(self):
        return self.nome

# Model para representar o Mentee (Mentorado)
class Mentee(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    bio = models.TextField()  
    telefone = models.CharField(max_length=20, blank=True, null=True) 
    data_criacao = models.DateField(auto_now_add=True)  

    def __str__(self):
        return self.nome

# Model para representar a Sessão de Mentoria
class SessaoMentoria(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.DO_NOTHING, related_name='sessoes')
    mentee = models.ForeignKey(Mentee, on_delete=models.DO_NOTHING, related_name='sessoes')
    data_sessao = models.DateTimeField()  
    duracao = models.PositiveIntegerField()  
    assunto = models.CharField(max_length=255)  
    notas = models.TextField(blank=True, null=True) 
    status = models.CharField(max_length=100, choices=[('agendada', 'Agendada'), ('realizada', 'Realizada'), ('cancelada', 'Cancelada')], default='agendada')

    def __str__(self):
        return f"Sessão de Mentoria entre {self.mentor.nome} e {self.mentee.nome}"

# Model para representar o Feedback após a mentoria
class Feedback(models.Model):
    sessao = models.ForeignKey(SessaoMentoria, on_delete=models.DO_NOTHING, related_name='feedback')
    mentee = models.ForeignKey(Mentee, on_delete=models.DO_NOTHING, related_name='feedback')
    nota = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)]) 
    comentario = models.TextField(blank=True, null=True)  sobre a sessão

    def __str__(self):
        return f"Feedback de {self.mentee.nome} para {self.sessao.mentor.nome}"

# Model para representar o Agendamento de Mentoria
class Agendamento(models.Model):
    mentee = models.ForeignKey(Mentee, on_delete=models.DO_NOTHING)
    mentor = models.ForeignKey(Mentor, on_delete=models.DO_NOTHING)
    data_agendada = models.DateTimeField()  
    status = models.CharField(max_length=100, choices=[('agendada', 'Agendada'), ('confirmada', 'Confirmada'), ('cancelada', 'Cancelada')], default='agendada')

    def __str__(self):
        return f"Agendamento de {self.mentee.nome} com {self.mentor.nome}"

from django.shortcuts import render, redirect
from .models import Curso, Categoria, Inscricao
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer



def Todos_cursos(request):
    cursos = Curso.objects.all()
    categorias = Categoria.objects.prefetch_related('cursos').all()
    return render(request, 'todos_cursos.html',{'cursos': cursos, 'categorias': categorias})


def detalhe_curso(request, id):
    detalhe_curso = get_object_or_404(Curso, id=id) 
    return render(request, 'detalhe_curso.html', {'detalhe_curso':detalhe_curso})


def incricao_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    return render(request, 'inscrever_curso.html', {'curso': curso})


def inscricao_create(request, id):
    curso = Curso.objects.get(id=id)

    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        data_nascimento = request.POST.get('data_nascimento')
        cidade = request.POST.get('cidade')
        bairro = request.POST.get('bairro')
        pais = request.POST.get('pais')
        codigo_postal = request.POST.get('codigo_postal')
        endereco = request.POST.get('endereco')
        genero = request.POST.get('genero')

        # Criação do objeto Inscricao
        inscricao = Inscricao(
            curso=curso,
            nome=nome,
            email=email,
            telefone=telefone,
            data_nascimento=data_nascimento,
            cidade=cidade,
            bairro=bairro,
            pais=pais,
            codigo_postal=codigo_postal,
            endereco=endereco,
            genero=genero,
            status='Pendente'  
        )

        inscricao.save()

        # Redireciona ou retorna uma resposta de sucesso
        return redirect('ficha_inscricao', id=inscricao.id)  # Supondo que você tenha uma URL de sucesso configurada

    else:
        return render(request, 'inscricao_form.html', {'curso': curso})


def ficha_inscricao(request, id):
    inscricao = get_object_or_404(Inscricao, id=id)
    curso = inscricao.curso  # Pegue o curso da inscrição
    instituicao = curso.instituicao  # Acesse a instituição do curso
    return render(request, 'ficha_inscricao.html', {'inscricao': inscricao, 'curso': curso, 'instituicao': instituicao})


def conformacao_mensagem(request, inscricao_id):
    inscricao = get_object_or_404(Inscricao, pk=inscricao_id)

    if not inscricao.email:
        return HttpResponse(f"A inscrição {inscricao.id} não tem um e-mail associado. Não foi possível enviar o e-mail.")
    
    if inscricao.status == 'Pendente':
        novo_status = 'Pendente'
        inscricao.status = novo_status
        inscricao.save()

        subject = '🔄 Sua Inscrição Está Sendo Processada - Educangola'
        message = f"""
        <h2>Olá {inscricao.nome},</h2>
        <p>Agradecemos por utilizar o <strong>Educangola</strong>!</p>
        <p>Informamos que sua inscrição no curso <strong>{inscricao.curso.nome}</strong> está sendo processada.</p>
        <p>Nos próximos dias, você receberá mais informações sobre a sua inscrição, incluindo o status da sua aprovação.</p>
        <p><strong>Detalhes do Curso:</strong><br>
        - <strong>Nome:</strong> {inscricao.curso.nome}<br>
        - <strong>Instituição:</strong> {inscricao.curso.instituicao.nome}<br>
        - <strong>Início:</strong> {inscricao.curso.data_inicio}<br>
        - <strong>Modalidade:</strong> {inscricao.curso.modalidade}</p>
        <p><strong>Equipe Educangola</strong></p>
        <p><em>Transformando o futuro da educação, um curso de cada vez.</em></p>
        """

    elif inscricao.status == 'Confirmada':
        novo_status = 'Confirmada'
        inscricao.status = novo_status
        inscricao.save()

        subject = '🎉 Sua Inscrição foi Confirmada! Bem-vindo ao Educangola!'
        message = f"""
        <h2>Olá {inscricao.nome},</h2>
        <p>Temos o prazer de informar que sua inscrição no curso <strong>{inscricao.curso.nome}</strong> foi <strong>confirmada!</strong></p>
        <p>Agradecemos por escolher o <strong>Educangola</strong> para impulsionar sua carreira e aprendizado. Estamos empolgados em tê-lo conosco em nosso ambiente de ensino.</p>
        <p><strong>Detalhes do Curso:</strong><br>
        - <strong>Nome:</strong> {inscricao.curso.nome}<br>
        - <strong>Instituição:</strong> {inscricao.curso.instituicao.nome}<br>
        - <strong>Início:</strong> {inscricao.curso.data_inicio}<br>
        - <strong>Modalidade:</strong> {inscricao.curso.modalidade}</p>
        <p>Em breve, você receberá mais detalhes sobre o cronograma do curso e outras informações importantes.</p>
        <p><strong>Equipe Educangola</strong></p>
        <p><em>Transformando o futuro da educação, um curso de cada vez.</em></p>
        """
    
    elif inscricao.status == 'Cancelada':
        novo_status = 'Cancelada'
        inscricao.status = novo_status
        inscricao.save()

        subject = '❌ Sua Inscrição foi Negada - Educangola'
        message = f"""
        <h2>Olá {inscricao.nome},</h2>
        <p>Lamentamos informar que sua inscrição no curso <strong>{inscricao.curso.nome}</strong> foi <strong>negada</strong>.</p>
        <p>Infelizmente, sua inscrição não foi aceita neste momento. Se você tiver dúvidas ou gostaria de mais informações sobre o motivo da negação, entre em contato conosco.</p>
        <p><strong>Detalhes do Curso:</strong><br>
        - <strong>Nome:</strong> {inscricao.curso.nome}<br>
        - <strong>Instituição:</strong> {inscricao.curso.instituicao.nome}</p>
        <p>Esperamos que, no futuro, você possa ter uma nova oportunidade de participar do <strong>Educangola</strong>.</p>
        <p><strong>Equipe Educangola</strong></p>
        <p><em>Transformando o futuro da educação, um curso de cada vez.</em></p>
        """

    send_mail(
        subject,
        message, 
        settings.DEFAULT_FROM_EMAIL,
        [inscricao.email],
        html_message=message  
    )

    # Agora, vamos enviar a mensagem em tempo real via WebSocket
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'mensagens_group',  
        {
            'type': 'mensagem_enviada', 
            'message': f"O status da inscrição {inscricao.id} foi alterado para {inscricao.status}."
        }
    )

    cursos = Curso.objects.all()
    categorias = Categoria.objects.prefetch_related('cursos').all()
    return render(request, 'todos_cursos.html',{'cursos': cursos, 'categorias': categorias})


def instrutor(request):
    pass
# Generated by Django 5.1.4 on 2024-12-27 01:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_habilidade_tutor'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopicoEstudo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='GrupoEstudo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('ativo', models.BooleanField(default=True)),
                ('membros', models.ManyToManyField(related_name='grupos', to='usuarios.usuario')),
                ('topicos', models.ManyToManyField(blank=True, related_name='grupos', to='usuarios.topicoestudo')),
            ],
        ),
        migrations.CreateModel(
            name='MaterialEstudo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('arquivo', models.FileField(upload_to='materiais_estudo/')),
                ('data_upload', models.DateTimeField(auto_now_add=True)),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materiais', to='usuarios.grupoestudo')),
            ],
        ),
        migrations.CreateModel(
            name='SessaoEstudo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_sessao', models.DateTimeField()),
                ('local', models.CharField(max_length=255)),
                ('duracao', models.PositiveIntegerField()),
                ('descricao', models.TextField(blank=True, null=True)),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessoes', to='usuarios.grupoestudo')),
                ('topico', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuarios.topicoestudo')),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackSessao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('comentario', models.TextField(blank=True, null=True)),
                ('membro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks', to='usuarios.usuario')),
                ('sessao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks', to='usuarios.sessaoestudo')),
            ],
        ),
    ]

# Generated by Django 5.1.4 on 2024-12-27 01:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0003_topicoestudo_grupoestudo_materialestudo_sessaoestudo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hackathon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('data_inicio', models.DateTimeField()),
                ('data_fim', models.DateTimeField()),
                ('local', models.CharField(blank=True, max_length=255, null=True)),
                ('ativo', models.BooleanField(default=True)),
                ('criador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hackathons', to='usuarios.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('hackathon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipes', to='hackathons.hackathon')),
            ],
        ),
        migrations.CreateModel(
            name='Desafio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('data_inicio', models.DateTimeField()),
                ('data_fim', models.DateTimeField()),
                ('hackathon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='desafios', to='hackathons.hackathon')),
            ],
        ),
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inscricao_data', models.DateTimeField(auto_now_add=True)),
                ('equipe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hackathons.equipe')),
                ('hackathon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participantes', to='hackathons.hackathon')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='equipe',
            name='membros',
            field=models.ManyToManyField(related_name='equipes', to='hackathons.participante'),
        ),
        migrations.CreateModel(
            name='Submissao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_submissao', models.DateTimeField(auto_now_add=True)),
                ('arquivo', models.FileField(blank=True, null=True, upload_to='submissoes/')),
                ('descricao', models.TextField(blank=True, null=True)),
                ('desafio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissoes', to='hackathons.desafio')),
                ('equipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissoes', to='hackathons.equipe')),
            ],
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')])),
                ('comentario', models.TextField(blank=True, null=True)),
                ('juiz', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='avaliacoes', to='usuarios.usuario')),
                ('submissao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avaliacoes', to='hackathons.submissao')),
            ],
        ),
    ]

# Generated by Django 5.1.4 on 2024-12-28 14:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True, verbose_name='Nome da Tag')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('conteudo', models.TextField()),
                ('data_publicacao', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('publicado', models.BooleanField(default=False)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='noticias.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=100)),
                ('conteudo', models.TextField()),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('aprovado', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='noticias.post')),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255, verbose_name='Título da Notícia')),
                ('resumo', models.CharField(blank=True, max_length=500, null=True, verbose_name='Resumo da Notícia')),
                ('conteudo', models.TextField(verbose_name='Conteúdo')),
                ('autor', models.CharField(max_length=255, verbose_name='Autor')),
                ('autor_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail do Autor')),
                ('data_publicacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Publicação')),
                ('data_atualizacao', models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='noticias/', verbose_name='Imagem Principal')),
                ('imagem_alternativa', models.ImageField(blank=True, null=True, upload_to='noticias/', verbose_name='Imagem Alternativa')),
                ('fonte', models.URLField(blank=True, null=True, verbose_name='Fonte')),
                ('video_url', models.URLField(blank=True, null=True, verbose_name='URL do Vídeo')),
                ('localizacao', models.CharField(blank=True, max_length=255, null=True, verbose_name='Localização')),
                ('destaque', models.BooleanField(default=False, verbose_name='Destacar Notícia')),
                ('status', models.CharField(choices=[('Publicado', 'Publicado'), ('Em revisão', 'Em revisão'), ('Arquivado', 'Arquivado')], default='Publicado', max_length=20, verbose_name='Status')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='noticias', to='noticias.categoria', verbose_name='Categoria')),
                ('leitura_recomendada', models.ManyToManyField(blank=True, to='noticias.noticia', verbose_name='Leitura Recomendada')),
                ('noticias_relacionadas', models.ManyToManyField(blank=True, to='noticias.noticia', verbose_name='Notícias Relacionadas')),
                ('tags', models.ManyToManyField(blank=True, to='noticias.tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Notícia',
                'verbose_name_plural': 'Notícias',
            },
        ),
    ]

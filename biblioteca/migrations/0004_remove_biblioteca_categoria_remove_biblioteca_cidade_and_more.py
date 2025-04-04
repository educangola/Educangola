# Generated by Django 5.1.4 on 2025-02-05 21:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0003_categorialivro_alter_biblioteca_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biblioteca',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='biblioteca',
            name='cidade',
        ),
        migrations.RemoveField(
            model_name='biblioteca',
            name='data_criacao',
        ),
        migrations.RemoveField(
            model_name='biblioteca',
            name='endereco',
        ),
        migrations.RemoveField(
            model_name='biblioteca',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='biblioteca',
            name='site',
        ),
        migrations.RemoveField(
            model_name='biblioteca',
            name='telefone',
        ),
        migrations.CreateModel(
            name='PerfilBiblioteca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco', models.CharField(max_length=255)),
                ('cidade', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=20)),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('site', models.URLField(blank=True, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='bibliotecas/logos/')),
                ('biblioteca', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.biblioteca')),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='biblioteca.categoriabiblioteca')),
            ],
            options={
                'verbose_name': 'Perfil da Biblioteca',
                'verbose_name_plural': 'Perfis das Bibliotecas',
            },
        ),
    ]

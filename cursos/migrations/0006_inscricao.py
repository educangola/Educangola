# Generated by Django 5.1.4 on 2025-01-19 17:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0005_alter_curso_preco'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(blank=True, max_length=20, null=True)),
                ('data_inscricao', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pendente', 'Pendente'), ('Confirmada', 'Confirmada'), ('Cancelada', 'Cancelada')], default='Pendente', max_length=50)),
                ('observacoes', models.TextField(blank=True, null=True)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inscricoes', to='cursos.curso')),
            ],
        ),
    ]

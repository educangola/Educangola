# Generated by Django 5.1.4 on 2025-01-21 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0007_inscricao_bairro_inscricao_cidade_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='data_criacao',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]

# Generated by Django 5.1.4 on 2024-12-28 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instituicoes', '0003_alter_curso_categoria_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='instituicoes/logos/'),
        ),
    ]

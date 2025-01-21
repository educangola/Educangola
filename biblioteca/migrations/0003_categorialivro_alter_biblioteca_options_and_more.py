# Generated by Django 5.1.4 on 2024-12-28 10:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0002_consultoriatcc_tese_emprestimotese'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaLivro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Categoria de Livro',
                'verbose_name_plural': 'Categorias de Livros',
            },
        ),
        migrations.AlterModelOptions(
            name='biblioteca',
            options={'verbose_name': 'Biblioteca', 'verbose_name_plural': 'Bibliotecas'},
        ),
        migrations.AlterModelOptions(
            name='categoriabiblioteca',
            options={'verbose_name': 'Categoria da Biblioteca', 'verbose_name_plural': 'Categorias das Bibliotecas'},
        ),
        migrations.AlterModelOptions(
            name='consultoriatcc',
            options={'verbose_name': 'Consultoria de TCC', 'verbose_name_plural': 'Consultorias de TCC'},
        ),
        migrations.AlterModelOptions(
            name='emprestimo',
            options={'verbose_name': 'Empréstimo', 'verbose_name_plural': 'Empréstimos'},
        ),
        migrations.AlterModelOptions(
            name='emprestimotese',
            options={'verbose_name': 'Empréstimo de Tese', 'verbose_name_plural': 'Empréstimos de Teses'},
        ),
        migrations.AlterModelOptions(
            name='livro',
            options={'verbose_name': 'Livro', 'verbose_name_plural': 'Livros'},
        ),
        migrations.AlterModelOptions(
            name='tese',
            options={'verbose_name': 'Tese', 'verbose_name_plural': 'Teses'},
        ),
        migrations.AlterModelOptions(
            name='usuariobiblioteca',
            options={'verbose_name': 'Usuário da Biblioteca', 'verbose_name_plural': 'Usuários da Biblioteca'},
        ),
        migrations.AlterField(
            model_name='consultoriatcc',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='consultorias', to='biblioteca.usuariobiblioteca'),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='livro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='biblioteca.livro'),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='biblioteca.usuariobiblioteca'),
        ),
        migrations.AlterField(
            model_name='emprestimotese',
            name='tese',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='biblioteca.tese'),
        ),
        migrations.AlterField(
            model_name='emprestimotese',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='biblioteca.usuariobiblioteca'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='biblioteca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='livros', to='biblioteca.biblioteca'),
        ),
        migrations.AlterField(
            model_name='tese',
            name='biblioteca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='teses', to='biblioteca.biblioteca'),
        ),
        migrations.AlterField(
            model_name='usuariobiblioteca',
            name='biblioteca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='usuarios', to='biblioteca.biblioteca'),
        ),
        migrations.AddField(
            model_name='livro',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='biblioteca.categorialivro'),
        ),
    ]

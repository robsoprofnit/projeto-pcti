# Generated by Django 4.0 on 2021-12-28 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ano_base',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.PositiveIntegerField()),
                ('_delete', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Dimensoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=256)),
                ('descricao', models.TextField()),
                ('_delete', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('_delete', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Regiao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('_delete', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Responsavel_instituicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_instituicao', models.IntegerField()),
                ('id_responsavel', models.IntegerField()),
                ('_delete', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('_delete', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Variavel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=256)),
                ('descricao', models.TextField()),
                ('tag', models.CharField(max_length=50)),
                ('_delete', models.BooleanField()),
                ('id_dimensao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.dimensoes')),
            ],
        ),
        migrations.CreateModel(
            name='Uf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sigla', models.CharField(max_length=2)),
                ('_delete', models.BooleanField()),
                ('id_regiao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.regiao')),
            ],
        ),
        migrations.CreateModel(
            name='Sub_indicadores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.TextField()),
                ('_delete', models.BooleanField()),
                ('id_dimensao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.dimensoes')),
            ],
        ),
        migrations.CreateModel(
            name='Respostas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resposta', models.CharField(max_length=256)),
                ('data_resposta', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('tag', models.CharField(max_length=50)),
                ('id_instituicao', models.IntegerField()),
                ('id_respondido_por', models.IntegerField()),
                ('_delete', models.BooleanField()),
                ('id_ano_base', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.ano_base')),
                ('id_variavel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.variavel')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=256)),
                ('cpf_cnpj', models.CharField(max_length=50)),
                ('razao_social', models.CharField(max_length=256)),
                ('nome_social', models.CharField(max_length=256)),
                ('id_email', models.EmailField(max_length=254)),
                ('_delete', models.BooleanField()),
                ('id_tipo_pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.tipo_pessoa')),
                ('id_uf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.uf')),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('_delete', models.BooleanField()),
                ('id_uf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.uf')),
            ],
        ),
    ]

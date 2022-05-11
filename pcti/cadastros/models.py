from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


# Create your models here.

# Create Ano Base Model
class Ano_base(models.Model):
    class Meta:
        verbose_name_plural = "Anos Base"

    ano = models.PositiveIntegerField(verbose_name='Ano')
    desativar = models.BooleanField()

    def __str__(self):
        return '{}'.format(self.ano)


# Create Região Model
class Regiao(models.Model):
    class Meta:
        verbose_name_plural = "Regiões"

    nome = models.CharField(max_length=50, verbose_name='Região Geográfica')
    desativar = models.BooleanField()

    def __str__(self):
        return '{}'.format(self.nome)


# Create Tipo Esfera da Instituição Model
class Tipo_esfera(models.Model):
    class Meta:
        verbose_name_plural = "Tipos de Esferas"

    nome = models.CharField(max_length=50, verbose_name='Tipo Esfera')
    desativar = models.BooleanField()

    def __str__(self):
        return '{}'.format(self.nome)


# Create Dimensões Model
class Dimensoes(models.Model):
    class Meta:
        verbose_name_plural = "Dimensões"

    nome = models.CharField(max_length=256, verbose_name='Dimensão')
    descricao = models.TextField(verbose_name='Descrição da Dimensão')
    desativar = models.BooleanField()

    def __str__(self):
        return '{}'.format(self.nome)


# Create Uf Model
class Uf(models.Model):
    class Meta:
        verbose_name_plural = "Estados"

    nome = models.CharField(max_length=50, verbose_name='Estado')
    sigla = models.CharField(max_length=2, verbose_name='Sigla UF')
    desativar = models.BooleanField()

    id_regiao = models.ForeignKey(Regiao, on_delete=models.PROTECT, verbose_name='Região Geográfica')

    def __str__(self):
        return '{}'.format(self.nome)


# Create Municipio Model
class Municipio(models.Model):
    class Meta:
        verbose_name_plural = "Municípios"

    nome = models.CharField(max_length=50, verbose_name='Município')
    desativar = models.BooleanField()

    id_uf = models.ForeignKey(Uf, on_delete=models.PROTECT, verbose_name='UF')

    def __str__(self):
        return '{} - {}'.format(self.nome, self.id_uf)


# Create Pessoa Model
class Pessoa(models.Model):
    class Meta:
        verbose_name_plural = "Pessoas"

    nome = models.CharField(max_length=256, verbose_name='Nome completo')
    cpf = models.CharField(max_length=14, null=True, verbose_name='CPF')
    nome_social = models.CharField(max_length=256, blank=True, verbose_name='Nome Social')
    desativar = models.BooleanField()

    id_municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT, verbose_name='Município')
    id_user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Usuário')

    def __str__(self):
        return '{}'.format(self.nome)


# Create Pessoa Jurídica Model
class Pessoa_juridica(models.Model):
    class Meta:
        verbose_name_plural = "Pessoas Jurídicas"

    nome = models.CharField(max_length=256, verbose_name='Nome')
    cnpj = models.CharField(max_length=50, verbose_name='CNPJ')
    razao_social = models.CharField(max_length=256, verbose_name='Razão Social')
    email = models.CharField(max_length=150, verbose_name='Email')
    desativar = models.BooleanField()

    id_tipo_esfera = models.ForeignKey(Tipo_esfera, on_delete=models.PROTECT, verbose_name='Tipo Esfera')
    id_municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT, verbose_name='Município')

    def __str__(self):
        return '{}'.format(self.nome)


# Create Vinculo Responsável da Instituição Model
class Responsavel_instituicao(models.Model):
    class Meta:
        verbose_name_plural = "Responsáveis Instituição"

    desativar = models.BooleanField()

    id_pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT, verbose_name='Pessoa Responsável')
    id_pessoa_juridica = models.ForeignKey(Pessoa_juridica, on_delete=models.PROTECT, verbose_name='Instituição')

    def __str__(self):
        return '{} - {}'.format(self.id_pessoa, self.id_pessoa_juridica)


# Create Variavel Model
class Variavel(models.Model):
    class Meta:
        verbose_name_plural = "Variáveis"

    nome = models.CharField(max_length=256, verbose_name='Variável')
    descricao = models.TextField(verbose_name='Descrição da Variável')
    tag = models.CharField(max_length=50, verbose_name='#TAG')
    desativar = models.BooleanField()

    id_dimensao = models.ForeignKey(Dimensoes, on_delete=models.PROTECT, verbose_name='Dimensão')

    def __str__(self):
        return '{}'.format(self.nome)


# Create Sub-Indicadores Model
class Sub_indicadores(models.Model):
    class Meta:
        verbose_name_plural = "Sub Indicadores"

    nome = models.CharField(max_length=250, verbose_name='Sub-Indicador')
    descricao = models.TextField(verbose_name='Descrição do Sub-Indicador')
    desativar = models.BooleanField()

    id_dimensao = models.ForeignKey(Dimensoes, on_delete=models.PROTECT, verbose_name='Dimensão')

    def __str__(self):
        return '{}'.format(self.nome)


# Create Relatórios Anuais Model
class Relatorios(models.Model):
    class Meta:
        verbose_name_plural = "Relatórios"

    desativar = models.BooleanField()

    id_pessoa_juridica = models.ForeignKey(Pessoa_juridica, on_delete=models.PROTECT, verbose_name='Instituição')
    id_ano = models.ForeignKey(Ano_base, on_delete=models.PROTECT, verbose_name='Ano')
    id_dimensao = models.ForeignKey(Dimensoes, on_delete=models.PROTECT, verbose_name='Dimensão')
    id_user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Usuário')

    def __str__(self):
        return '{} - {} - {}'.format(self.id_pessoa_juridica, self.id_ano, self.id_dimensao)


# Create Respostas Model
class Respostas(models.Model):
    class Meta:
        verbose_name_plural = "Respostas"

    resposta = models.CharField(max_length=256, verbose_name='Resposa')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Data de cadastro')
    data_atualizacao = models.DateTimeField(auto_now=True, null=True, verbose_name='Ultima alteração')
    tag = models.CharField(max_length=50, verbose_name='#TAG')
    desativar = models.BooleanField()

    id_ano_base = models.ForeignKey(Ano_base, on_delete=models.CASCADE, verbose_name='Ano')
    id_pessoa_juridica = models.ForeignKey(Pessoa_juridica, related_name='instituicao',
                                           on_delete=models.CASCADE, verbose_name='Instituição')
    id_pessoa = models.ForeignKey(Pessoa, related_name='responsavel',
                                  on_delete=models.CASCADE, verbose_name='Responsável')
    id_user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Usuário')
    id_variavel = models.ForeignKey(Variavel, on_delete=models.CASCADE, verbose_name='Variável')
    id_relatorio = models.ForeignKey(Relatorios, on_delete=models.CASCADE, verbose_name='Relatório')
    id_dimensao = models.ForeignKey(Dimensoes, on_delete=models.CASCADE, verbose_name='Dimensão')

    def __str__(self):
        return '{} ({} - {})'.format(self.resposta, self.tag, self.id_ano_base)


# Create Grupo de Variáveis, Sub-indicadores e Dimensções Model
class Grupo_variavel_subind(models.Model):
    class Meta:
        verbose_name_plural = "Grupo_variavel_subind"

    desativar = models.BooleanField()

    id_variavel = models.ForeignKey(Variavel, on_delete=models.PROTECT, verbose_name='Variável')
    id_sub_indicador = models.ForeignKey(Sub_indicadores, on_delete=models.PROTECT, verbose_name='Indicadores')
    id_dimensao = models.ForeignKey(Dimensoes, on_delete=models.PROTECT, verbose_name='Dimensões')

    def __str__(self):
        return '{} - {} - {}'.format(self.id_dimensao, self.id_sub_indicador, self.id_variavel)


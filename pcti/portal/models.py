from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

# Create Ano Base Model
class Ano_base(models.Model):
    class Meta:
        verbose_name_plural = "Anos Base"
    ano = models.PositiveIntegerField(verbose_name='Ano')
    _delete = models.BooleanField()

    def __str__(self):
        return '{}'.format(self.ano)


# Create Região Model
class Regiao(models.Model):
    class Meta:
        verbose_name_plural = "Regiões"
    nome = models.CharField(max_length=50, verbose_name='Região Geográfica')
    _delete = models.BooleanField()

    def __str__(self):
        return '{}'.format(self.nome)


# Create Uf Model
class Uf(models.Model):
    class Meta:
        verbose_name_plural = "Estados"
    nome = models.CharField(max_length=50, verbose_name='Estado')
    sigla = models.CharField(max_length=2, verbose_name='Sigla UF')
    id_regiao = models.ForeignKey(Regiao, on_delete=models.PROTECT, verbose_name='Região Geográfica')
    _delete = models.BooleanField()

    def __str__(self):
        return '{}'.format(self.nome)


# Create Municipio Model
class Municipio(models.Model):
    class Meta:
        verbose_name_plural = "Municípios"
    nome = models.CharField(max_length=50, verbose_name='Município')
    id_uf = models.ForeignKey(Uf, on_delete=models.PROTECT, verbose_name='UF')
    _delete = models.BooleanField()

    def __str__(self):
        return '{} - {}'.format(self.nome, self.id_uf)


# Create Tipo Esfera da Instituição Model
class Tipo_esfera(models.Model):
    class Meta:
        verbose_name_plural = "Tipos de Esferas"
    nome = models.CharField(max_length=50, verbose_name='Tipo Esfera')
    _delete = models.BooleanField()

    def __str__(self):
        return '{}'.format(self.nome)


# Create Email Model
class Email(models.Model):
    class Meta:
        verbose_name_plural = "Emails"
    email = models.EmailField()
    _delete = models.BooleanField()

    def __str__(self):
        return '{}'.format(self.email)


# Create Pessoa Model
class PF(models.Model):
    class Meta:
        verbose_name_plural = "Pessoas Físicas"
    nome = models.CharField(max_length=256, verbose_name='Nome completo')
    cpf = models.CharField(max_length=50, verbose_name='CPF')
    nome_social = models.CharField(max_length=256, blank=True, verbose_name='Nome Social')
    id_email = models.ForeignKey(Email, on_delete=models.PROTECT, verbose_name='Email')
    _delete = models.BooleanField()

    def __str__(self):
        return '{}'.format(self.nome)


# Create Pessoa Jurídica Model
class PJ(models.Model):
    class Meta:
        verbose_name_plural = "Pessoas Jurídicas"
    nome = models.CharField(max_length=256, verbose_name='Nome')
    cnpj = models.CharField(max_length=50, verbose_name='CNPJ')
    razao_social = models.CharField(max_length=256, verbose_name='Razão Social')
    id_email = models.ForeignKey(Email, on_delete=models.PROTECT, verbose_name='Email')
    id_tipo_esfera = models.ForeignKey(Tipo_esfera, on_delete=models.PROTECT, verbose_name='Tipo Esfera')
    id_uf = models.ForeignKey(Uf, on_delete=models.PROTECT, verbose_name='UF')
    id_municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT, verbose_name='Município')
    _delete = models.BooleanField()

    def __str__(self):
        return '{}'.format(self.nome)


# Integração User x Pessoa Model
class User_pessoa(models.Model):
    class Meta:
        verbose_name_plural = "Users_Pessoas"
    id_user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Usuário')
    id_pessoa = models.ForeignKey(PF, on_delete=models.PROTECT, verbose_name='Nome do Usuário')
    _delete = models.BooleanField()

    def __str__(self):
        return '{} - {}'.format(self.id_user, self.id_pessoa)


# Create Vinculo Responsável da Instituição Model
class Responsavel_instituicao(models.Model):
    class Meta:
        verbose_name_plural = "Responsáveis Instituição"
    id_instituicao = models.ForeignKey(PJ, on_delete=models.PROTECT, verbose_name='Instituição')
    id_responsavel = models.ForeignKey(PF, on_delete=models.PROTECT, verbose_name='Nome do Responsável')
    _delete = models.BooleanField()

    def __str__(self):
        return '{} - {}'.format(self.id_instituicao, self.id_responsavel)


# Create Dimensões Model
class Dimensoes(models.Model):
    class Meta:
        verbose_name_plural = "Dimensões"
    nome = models.CharField(max_length=256, verbose_name='Dimensão')
    descricao = models.TextField(verbose_name='Descrição da Dimensão')
    _delete = models.BooleanField()

    def __str__(self):
        return '{}'.format(self.nome)


# Create Variavel Model
class Variavel(models.Model):
    class Meta:
        verbose_name_plural = "Variáveis"
    nome = models.CharField(max_length=256, verbose_name='Variável')
    descricao = models.TextField(verbose_name='Descrição da Variável')
    tag = models.CharField(max_length=50, verbose_name='#TAG')
    id_dimensao = models.ForeignKey(Dimensoes, on_delete=models.PROTECT, verbose_name='Dimensão')
    _delete = models.BooleanField()

    def __str__(self):
        return '{}'.format(self.nome)


# Create Sub-Indicadores Model
class Sub_indicadores(models.Model):
    class Meta:
        verbose_name_plural = "Sub Indicadores"
    nome = models.CharField(max_length=50, verbose_name='Sub-Indicador')
    descricao = models.TextField(verbose_name='Descrição do Sub-Indicador')
    id_dimensao = models.ForeignKey(Dimensoes, on_delete=models.PROTECT, verbose_name='Dimensão')
    _delete = models.BooleanField()

    def __str__(self):
        return '{}'.format(self.nome)


# Create Relatórios Anuais Model
class Relatorios(models.Model):
    class Meta:
        verbose_name_plural = "Relatórios"
    id_instituicao = models.ForeignKey(PJ, on_delete=models.PROTECT, verbose_name='Instituição')
    id_ano = models.ForeignKey(Ano_base, on_delete=models.PROTECT, verbose_name='Ano')
    id_dimensao = models.ForeignKey(Dimensoes, on_delete=models.PROTECT, verbose_name='Dimensão')
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    _delete = models.BooleanField()

    def __str__(self):
        return '{} - {} - {}'.format(self.id_instituicao, self.id_ano, self.id_dimensao)


# Create Respostas Model
class Respostas(models.Model):
    class Meta:
        verbose_name_plural = "Respostas"
    resposta = models.CharField(max_length=256, verbose_name='Resposa')
    data_resposta = models.DateTimeField(auto_now_add=True, verbose_name='Data de cadastro')
    data_atualizacao = models.DateTimeField(auto_now=True, null=True, verbose_name='Ultima alteração')
    tag = models.CharField(max_length=50, verbose_name='#TAG')
    id_ano_base = models.ForeignKey(Ano_base, on_delete=models.PROTECT, verbose_name='Ano')
    id_instituicao = models.ForeignKey(PJ, related_name='instituicao', on_delete=models.PROTECT, verbose_name='Instituição')
    id_respondido_por = models.ForeignKey(PF, related_name='responsavel', on_delete=models.PROTECT, verbose_name='Responsável')
    id_variavel = models.ForeignKey(Variavel, on_delete=models.PROTECT, verbose_name='Variável')
    id_relatorio = models.ForeignKey(Relatorios, on_delete=models.PROTECT, verbose_name='Relatório')
    _delete = models.BooleanField()

    def __str__(self):
        return '{} ({} - {})'.format(self.resposta, self.tag, self.id_ano_base)

from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

# Create Ano Base Model
class Ano_base(models.Model):
    ano = models.PositiveIntegerField()
    _delete = models.BooleanField()

    def __str__(self):
        return str(self.ano)


# Create Região Model
class Regiao(models.Model):
    nome = models.CharField(max_length=50)
    _delete = models.BooleanField()

    def __str__(self):
        return self.nome


# Create Uf Model
class Uf(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)
    id_regiao = models.ForeignKey(Regiao, on_delete=models.CASCADE)
    _delete = models.BooleanField()

    def __str__(self):
        return self.nome


# Create Municipio Model
class Municipio(models.Model):
    nome = models.CharField(max_length=50)
    id_uf = models.ForeignKey(Uf, on_delete=models.CASCADE)
    _delete = models.BooleanField()

    def __str__(self):
        return self.nome


# Create Tipo pessoa Model
class Tipo_pessoa(models.Model):
    nome = models.CharField(max_length=50)
    _delete = models.BooleanField()

    def __str__(self):
        return self.nome


# Create Email Model
class Email(models.Model):
    email = models.EmailField()
    _delete = models.BooleanField()

    def __str__(self):
        return self.email


# Create Pessoa Model
class Pessoa(models.Model):
    nome = models.CharField(max_length=256)
    cpf_cnpj = models.CharField(max_length=50)
    razao_social = models.CharField(max_length=256)
    nome_social = models.CharField(max_length=256)
    id_email = models.ForeignKey(Email, on_delete=models.CASCADE)
    id_tipo_pessoa = models.ForeignKey(Tipo_pessoa, on_delete=models.CASCADE)
    id_uf = models.ForeignKey(Uf, on_delete=models.CASCADE)
    _delete = models.BooleanField()

    def __str__(self):
        return self.nome


# Integração User x Pessoa Model
class User_pessoa(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    _delete = models.BooleanField()

    def __str__(self):
        return str(self.id_user)


# Create Vinculo Responsável da Instituição Model
class Responsavel_instituicao(models.Model):
    id_instituicao = models.ForeignKey(Pessoa, related_name='instituicao1', on_delete=models.CASCADE)
    id_responsavel = models.ForeignKey(Pessoa, related_name='responsavel1', on_delete=models.CASCADE)
    _delete = models.BooleanField()

    def __str__(self):
        return str(self.id_instituicao)


# Create Dimensões Model
class Dimensoes(models.Model):
    nome = models.CharField(max_length=256)
    descricao = models.TextField()
    _delete = models.BooleanField()

    def __str__(self):
        return self.nome


# Create Variavel Model
class Variavel(models.Model):
    nome = models.CharField(max_length=256)
    descricao = models.TextField()
    tag = models.CharField(max_length=50)
    id_dimensao = models.ForeignKey(Dimensoes, on_delete=models.CASCADE)
    _delete = models.BooleanField()

    def __str__(self):
        return self.nome


# Create Sub-Indicadores Model
class Sub_indicadores(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    id_dimensao = models.ForeignKey(Dimensoes, on_delete=models.CASCADE)
    _delete = models.BooleanField()

    def __str__(self):
        return self.nome


# Create Relatórios Anuais Model
class Relatorios(models.Model):
    id_instituicao = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    id_ano = models.ForeignKey(Ano_base, on_delete=models.CASCADE)
    id_dimensao = models.ForeignKey(Dimensoes, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    _delete = models.BooleanField()

    def __str__(self):
        return str(self.id_instituicao)


# Create Respostas Model
class Respostas(models.Model):
    resposta = models.CharField(max_length=256)
    data_resposta = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True, null=True)
    tag = models.CharField(max_length=50)
    id_ano_base = models.ForeignKey(Ano_base, on_delete=models.CASCADE)
    id_instituicao = models.ForeignKey(Pessoa, related_name='instituicao', on_delete=models.CASCADE)
    id_respondido_por = models.ForeignKey(Pessoa, related_name='responsavel', on_delete=models.CASCADE)
    id_variavel = models.ForeignKey(Variavel, on_delete=models.CASCADE)
    id_relatorio = models.ForeignKey(Relatorios, on_delete=models.CASCADE)
    _delete = models.BooleanField()

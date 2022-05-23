from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Ano_base)
admin.site.register(Regiao)
admin.site.register(Uf)
admin.site.register(Municipio)
admin.site.register(Tipo_esfera)
admin.site.register(Pessoa)
admin.site.register(Pessoa_juridica)
admin.site.register(Responsavel_instituicao)
admin.site.register(Dimensoes)
admin.site.register(GrupoIndicadores)
admin.site.register(Variavel)
admin.site.register(Indicadores)
admin.site.register(Respostas)
admin.site.register(Relatorios)


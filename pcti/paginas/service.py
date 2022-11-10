from cadastros.models import Respostas
from cadastros.models import (
    Respostas,
    Ano_base,
    Uf,
    Dimensoes,
    Indicadores,
    Pessoa_juridica,
)


def generate_dashboard_info():
    context = {}
    ano = Ano_base.objects.first()
    # DIMENSÃO RECURSO APLICADO
    dimensao_recurso_aplicado = Dimensoes.objects.filter(id=1).first()
    recurso_aplicado = Respostas.objects.filter(
        id_indicador=1,
        id_ano_base=ano,
        id_dimensao=dimensao_recurso_aplicado,
        id_pessoa_juridica=1,
    )
    recurso_aplicado_anos = []
    for resposta in recurso_aplicado:
        if resposta.id_ano_base not in recurso_aplicado_anos:
            recurso_aplicado_anos.append(resposta.id_ano_base)
    context["recurso_aplicado"] = recurso_aplicado
    context["recurso_aplicado_anos"] = recurso_aplicado_anos

    # DIMENSAO RH
    dimensao_rh = Dimensoes.objects.filter(id=2).first()
    context["rh"] = Respostas.objects.filter(
        id_indicador=15, id_ano_base=ano, id_dimensao=dimensao_rh, id_pessoa_juridica=1
    )
    rh_anos = []
    for resposta in context["rh"]:
        if resposta.id_ano_base not in rh_anos:
            rh_anos.append(resposta.id_ano_base)
    context["rh_anos"] = rh_anos

    # DIMENSAO BOLSA
    dimensao_bolsa = Dimensoes.objects.filter(id=3).first()
    bolsas = Respostas.objects.filter(
        id_indicador__in=[53, 54],
        id_ano_base=ano,
        id_dimensao=dimensao_bolsa,
        id_pessoa_juridica=1,
    )
    soma_53 = 0
    indicador_nome_53 = None
    indicador_nome_54 = None
    soma_54 = 0
    bolsa_anos = []
    for resposta in bolsas:
        if resposta.id_indicador.id == 53:
            soma_53 = soma_53 + resposta.resposta
            if indicador_nome_53 is None:
                indicador_nome_53 = resposta.id_indicador.nome
        else:
            soma_54 = soma_54 + resposta.resposta
            if indicador_nome_54 is None:
                indicador_nome_54 = resposta.id_indicador.nome
        if resposta.id_ano_base not in bolsa_anos:
            bolsa_anos.append(resposta.id_ano_base)
    context["bolsas_53"] = soma_53
    context["bolsas_54"] = soma_54
    context["nome_53"] = indicador_nome_53
    context["nome_54"] = indicador_nome_54
    context["bolsas_anos"] = bolsa_anos

    # DIMENSAO PATENTES
    dimensao_patentes = Dimensoes.objects.filter(id=5).first()
    context["patentes"] = Respostas.objects.filter(
        id_indicador=70,
        id_ano_base=ano,
        id_dimensao=dimensao_patentes,
        id_pessoa_juridica=1,
    )
    patentes_anos = []
    for resposta in context["patentes"]:
        if resposta.id_ano_base not in patentes_anos:
            patentes_anos.append(resposta.id_ano_base)
    context["patentes_anos"] = patentes_anos

    # DIMENSAO INOVAÇÃO
    dimensao_inovacao = Dimensoes.objects.filter(id=6).first()
    inovacao = Respostas.objects.filter(
        id_indicador=94,
        id_ano_base=ano,
        id_dimensao=dimensao_inovacao,
        id_pessoa_juridica=1,
    )
    # 1172, 1176, 1180 - Total de Empresas
    # 1173, 1177, 1181 - Total Produto ou Processo
    # 1174, 1178, 1182 - Total Produto
    # 1175, 1179, 1183 - Total Processo
    soma_empresas = 0
    inovacao_nome_empresas = "Total de Empresas"
    lista_empresas = [1172, 1176, 1180]

    soma_produto_processo = 0
    inovacao_nome_produto_processo = "Total Produto ou Processo"
    lista_produto_processo = [1173, 1177, 1181]

    soma_produto = 0
    inovacao_nome_produto = "Total Produto"
    lista_produto = [1174, 1178, 1182]

    soma_processo = 0
    inovacao_nome_processo = "Total Processo"
    lista_processo = [1175, 1179, 1183]

    patentes_anos = []

    for inova in inovacao:
        if inova.id_variavel.id in lista_empresas:
            soma_empresas = soma_empresas + inova.resposta

        elif inova.id_variavel.id in lista_produto_processo:
            soma_produto_processo = soma_produto_processo + inova.resposta

        elif inova.id_variavel.id in lista_produto:
            soma_produto = soma_produto + inova.resposta

        elif inova.id_variavel.id in lista_processo:
            soma_processo = soma_processo + inova.resposta

        if inova.id_ano_base not in patentes_anos:
            patentes_anos.append(resposta.id_ano_base)

    context["inovacao_anos"] = patentes_anos
    context["inovacao_empresas"] = soma_empresas
    context["inovacao_produto_processo"] = soma_produto_processo
    context["inovacao_produto"] = soma_produto
    context["inovacao_processo"] = soma_processo

    context["inovacao_nome_empresas"] = inovacao_nome_empresas
    context["inovacao_nome_produto_processo"] = inovacao_nome_produto_processo
    context["inovacao_nome_produto"] = inovacao_nome_produto
    context["inovacao_nome_processo"] = inovacao_nome_processo

    return context


def soma():
    pass

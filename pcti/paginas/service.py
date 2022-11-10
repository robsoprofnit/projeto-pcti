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

    # DIMENSAO PRODUÇÃO CIENTÍFICA
    dimensao_prod_cienc = Dimensoes.objects.filter(id=4).first()
    prod_cienc = Respostas.objects.filter(
        id_indicador=67,
        id_ano_base=ano,
        id_dimensao=dimensao_prod_cienc,
        id_pessoa_juridica=1,
    )   
    prod_cienc_anos = []

    soma_thompson_brasil = 0
    thompson_brasil = [829,830,831,832,833,834,835,836,837,838,839,840,841,842,843,844,845,846,847,848,849,850]
    soma_thompson_latina = 0
    thompson_latina = [851,852,853,854,855,856,857,858,859,860,861,862,863,864,865,866,867,868,869,870,871,872]
    soma_thompson_mundo = 0
    thompson_mundo = [873,874,875,876,877,878,879,880,881,882,883,884,885,886,887,888,889,890,891,892,893,894]

    soma_scopus_brasil = 0
    scopus_brasil = [895,896,897,898,899,900,901,902,903,904,905,906,907,908,909,910,911,912,913,914,915,916,917,918,919,920,921]
    soma_scopus_latina = 0
    scopus_latina = [922,923,924,925,926,927,928,929,930,931,932,933,934,935,936,937,938,939,940,941,942,943,944,945,946,947,948]
    soma_scopus_mundo = 0
    scopus_mundo = [949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975]

    for prod in prod_cienc:
        if prod.id_variavel.id in thompson_brasil:
            soma_thompson_brasil = soma_thompson_brasil + prod.resposta

        if prod.id_variavel.id in thompson_latina:
            soma_thompson_latina = soma_thompson_latina + prod.resposta

        if prod.id_variavel.id in thompson_mundo:
            soma_thompson_mundo = soma_thompson_mundo + prod.resposta

        if prod.id_variavel.id in scopus_brasil:
            soma_scopus_brasil = soma_scopus_brasil + prod.resposta

        if prod.id_variavel.id in scopus_latina:
            soma_scopus_latina = soma_scopus_latina + prod.resposta

        if prod.id_variavel.id in scopus_mundo:
            soma_scopus_mundo = soma_scopus_mundo + prod.resposta

        if prod.id_ano_base not in prod_cienc_anos:
            prod_cienc_anos.append(prod.id_ano_base)

    context["prod_cienc_anos"] = prod_cienc_anos
    context["soma_thompson_brasil"] = soma_thompson_brasil
    context["soma_thompson_latina"] = soma_thompson_latina
    context["soma_thompson_mundo"] = soma_thompson_mundo
    context["thompson_nome_brasil"] = "Thompson/ISI - Brasil"
    context["thompson_nome_latina"] = "Thompson/ISI - América Latina"
    context["thompson_nome_mundo"] = "Thompson/ISI - Mundo"

    context["soma_scopus_brasil"] = soma_scopus_brasil
    context["soma_scopus_latina"] = soma_scopus_latina
    context["soma_scopus_mundo"] = soma_scopus_mundo
    context["scopus_nome_brasil"] = "Scopus - Brasil"
    context["scopus_nome_latina"] = "Scopus - América Latina"
    context["scopus_nome_mundo"] = "Scopus - Mundo"

    return context


def soma():
    pass

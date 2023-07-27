from .views import lista_geral_recebimentos, lista_geral_despesas
from .models import Relatorio, ContasAVencer


def calcular_valor_total(request):

    try:
        relatorio_id = int(request.path.split('/')[-2])
        if relatorio_id:
            total_contas, total_recebimentos = 0, 0
            relatorio = Relatorio.objects.get(id=relatorio_id)
            for conta in relatorio.contas.all():
                total_contas += conta.valor

            for recebimento in relatorio.recebimentos.all():
                total_recebimentos += recebimento.valor_pagamento

            if total_contas is None:
                total_contas = 0
            if total_recebimentos is None:
                total_recebimentos = 0

            saldo_final = total_recebimentos - total_contas

            return total_contas, total_recebimentos, saldo_final
        else:
            return None, None, None
    except:
        return None, None, None


def valores(request):
    total_contas, total_recebimentos, saldo_final = calcular_valor_total(request)

    return {'total_contas': total_contas, 'total_recebimentos': total_recebimentos, 'saldo_final': saldo_final}


def saldo_despesas_recebimentos(request):
    try:
        user = request.user
        lista_despesas = lista_geral_despesas[user]
        lista_recebimentos = lista_geral_recebimentos[user]
        despesas_soma, recebimentos_soma = 0, 0
        for despesa in lista_despesas:
            despesas_soma += despesa[1]
        for recebimento in lista_recebimentos:
            recebimentos_soma += recebimento[1]
        saldo_final = recebimentos_soma - despesas_soma

        return saldo_final, recebimentos_soma, despesas_soma

    except:
        return None, None, None

def valor_saldo(request):
    saldofinal, recebimentos_soma, despesas_soma = saldo_despesas_recebimentos(request)

    return {'saldo_final_atual': saldofinal, 'recebimentos_soma': recebimentos_soma, 'despesas_soma': despesas_soma }


def lista_relatorios_usuario(request):
    try:
        user = request.user
        lista_relatorios = Relatorio.objects.filter(usuario=user).order_by("-data_lancamento")
        return {"lista_relatorios":lista_relatorios}
    except:
        lista_relatorios = []
        return {"lista_relatorios": lista_relatorios}


def lista_contas_a_vencer(request):
    try:
        user = request.user
        lista_contas_a_vencer = ContasAVencer.objects.filter(usuario=user).order_by("data_vencimento")
        return {"lista_contas_a_vencer": lista_contas_a_vencer}
    except:
        lista_contas_a_vencer = []
        return {"lista_contas_a_vencer": lista_contas_a_vencer}

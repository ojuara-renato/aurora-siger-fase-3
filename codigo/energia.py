def calcular_consumo_total(modulos):
    total=0
    for modulo in modulos.values():
        total+=modulo['consumo']
    return total

def calcular_consumo_essencial(modulos):
    total=0
    for modulo in modulos.values():
        if modulo['essencial']:
            total+=modulo['consumo']
    return total

def calcular_geracao_total(geracao):
    return geracao['solar']+geracao['eolica']

def calcular_balanco_energetico(geracao_total,consumo_total):
    return geracao_total-consumo_total

def atualizar_reserva(reserva_atual,balanco,capacidade_total):
    nova_reserva= reserva_atual+balanco*1

    if nova_reserva>capacidade_total:
        nova_reserva=capacidade_total
    elif nova_reserva<0:
        nova_reserva=0

    return nova_reserva

def verificar_reserva_baixa(reserva_atual,reserva_projetada,capacidade_total):
    limite= capacidade_total*.20

    return reserva_atual<=limite or reserva_projetada<=limite

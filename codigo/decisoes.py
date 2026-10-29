def avaliar_situacao_energetica(geracao_total,consumo_total,consumo_essencial,reserva_atual,reserva_projetada,capacidade_total):
    balanco= geracao_total-consumo_total
    limite= capacidade_total*.20
    reserva_baixa= reserva_atual<=limite or reserva_projetada<=limite
    energia_disponivel= geracao_total+reserva_atual
    situacao_critica= energia_disponivel<consumo_essencial
    recomendar_economia= (balanco<0 and reserva_baixa) or situacao_critica

    if situacao_critica:
        situacao='CRITICA'
    elif recomendar_economia:
        situacao='ECONOMIA'
    elif balanco<0:
        situacao='DEFICIT'
    elif reserva_baixa:
        situacao='RESERVA BAIXA'
    elif balanco>0:
        situacao='EXCEDENTE'
    else:
        situacao='NORMAL'

    return {'situacao':situacao,
            'reserva_baixa':reserva_baixa,
            'situacao_critica':situacao_critica,
            'recomendar_economia':recomendar_economia,
            'armazenar_excedente':balanco>0
            }

def verificar_deficit_previsto(geracao_prevista,consumo_total):
    return geracao_prevista < consumo_total

from dados import colonia,velocidades_vento,geracoes_eolicas,vento_previsto
from energia import calcular_consumo_total,calcular_consumo_essencial,calcular_geracao_total,calcular_balanco_energetico,atualizar_reserva
from previsao import prever_geracao_eolica,gerar_grafico_regressao
from decisoes import avaliar_situacao_energetica,verificar_deficit_previsto

def main():
    modulos=colonia['modulos'];geracao=colonia['energia']['geracao'];baterias=colonia['energia']['baterias']
    reserva_atual=baterias['reserva_atual'];capacidade_total=baterias['capacidade_total']
    consumo_total=calcular_consumo_total(modulos);consumo_essencial=calcular_consumo_essencial(modulos);geracao_total=calcular_geracao_total(geracao)
    balanco=calcular_balanco_energetico(geracao_total,consumo_total)
    reserva_projetada=atualizar_reserva(reserva_atual,balanco,capacidade_total)
    resultado=avaliar_situacao_energetica(geracao_total,consumo_total,consumo_essencial,reserva_atual,reserva_projetada,capacidade_total)
    reserva_com_economia=None
    if resultado['recomendar_economia']:
        balanco_economia=calcular_balanco_energetico(geracao_total,consumo_essencial)
        reserva_com_economia=atualizar_reserva(reserva_atual,balanco_economia,capacidade_total)
    previsao,inclinacao,intercepto=prever_geracao_eolica(velocidades_vento,geracoes_eolicas,vento_previsto)
    geracao_prevista=geracao['solar']+previsao
    deficit_previsto=verificar_deficit_previsto(geracao_prevista,consumo_total)
    gerar_grafico_regressao(velocidades_vento,geracoes_eolicas,inclinacao,intercepto,vento_previsto)
    print("\n=== MISSÃO AURORA SIGER - FASE 3 ===")
    print("\n--- BALANÇO ENERGÉTICO ---")
    print(f"Geração total: {geracao_total:.2f} kW")
    print(f"Consumo total: {consumo_total:.2f} kW")
    print(f"Balanço: {balanco:.2f} kW")
    print("\n--- RESERVA ENERGÉTICA ---")
    print(f"Reserva inicial: {reserva_atual:.2f} kWh")
    print(f"Reserva projetada sem economia: {reserva_projetada:.2f} kWh")
    print("\n--- PREVISÃO EÓLICA ---")
    print(f"Vento previsto: {vento_previsto} m/s")
    print(f"Geração eólica prevista: {previsao:.2f} kW")
    print(f"Geração total prevista: {geracao_prevista:.2f} kW")
    if deficit_previsto:
        print("ALERTA PREVENTIVO: possível déficit na próxima hora.")
    else:
        print("Previsão: geração suficiente para o consumo.")
    print("\n--- DECISÃO OPERACIONAL ---")
    print(f"Situação: {resultado['situacao']}")
    if resultado['reserva_baixa']:
        print("ALERTA: reserva atual ou projetada em 20% ou menos.")
    if resultado['situacao_critica']:
        disponivel = geracao_total + reserva_atual
        necessario = consumo_essencial
        print("ALERTA CRÍTICO: energia insuficiente para os módulos essenciais.")
        print(f"Energia disponível em 1 h: {disponivel:.2f} kWh")
        print(f"Energia necessária em 1 h: {necessario:.2f} kWh")
        print(f"Energia em falta: {necessario - disponivel:.2f} kWh")
    if resultado['recomendar_economia']:
        print("Recomendação: desligar temporariamente os módulos não essenciais.")
        print(f"Consumo original: {consumo_total:.2f} kW")
        print(f"Consumo hipotético com economia: {consumo_essencial:.2f} kW")
        print(f"Reserva projetada sem economia: {reserva_projetada:.2f} kWh")
        print(f"Reserva hipotética com economia: {reserva_com_economia:.2f} kWh")
        limite = capacidade_total * 0.20
        if reserva_atual > limite and reserva_projetada <= limite and reserva_com_economia > limite:
            print("A economia recomendada evitaria atingir o limite de 20%.")
    if resultado['armazenar_excedente']:
        print("Excedente disponível para armazenamento, até a capacidade das baterias.")
    print("\nGráfico salvo em: imagens/regressao_eolica.png")
if __name__ == '__main__':
    main()

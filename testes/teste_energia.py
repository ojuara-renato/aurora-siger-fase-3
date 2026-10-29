from codigo.dados import colonia
from codigo.energia import calcular_consumo_total, calcular_consumo_essencial, calcular_geracao_total, calcular_balanco_energetico, atualizar_reserva, verificar_reserva_baixa

def testar_calculos_energeticos():
    modulos = colonia["modulos"]
    geracao = colonia["energia"]["geracao"]
    assert calcular_consumo_total(modulos) == 45
    assert calcular_consumo_essencial(modulos) == 33
    total = calcular_geracao_total(geracao)
    assert total == 65
    balanco = calcular_balanco_energetico(total, 45)
    assert balanco == 20
    assert atualizar_reserva(120, balanco, 200) == 140
    assert atualizar_reserva(195,20,200) == 200
    assert atualizar_reserva(10,-30,200) == 0
    assert verificar_reserva_baixa(50,35,200) is True
    assert verificar_reserva_baixa(120,140,200) is False
    print("Testes energéticos: APROVADOS")

if __name__ == "__main__":
    testar_calculos_energeticos()

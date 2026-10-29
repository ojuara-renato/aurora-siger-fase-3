from codigo.decisoes import avaliar_situacao_energetica, verificar_deficit_previsto

def testar_decisoes():
    normal=avaliar_situacao_energetica(65,45,33,120,140,200)
    assert normal["situacao"] == "EXCEDENTE"
    assert normal["recomendar_economia"] is False
    assert normal["armazenar_excedente"] is True
    deficit=avaliar_situacao_energetica(40,45,33,120,115,200)
    assert deficit["situacao"] == "DEFICIT"
    assert deficit["recomendar_economia"] is False
    economia=avaliar_situacao_energetica(30,45,33,50,35,200)
    assert economia["situacao"] == "ECONOMIA"
    assert economia["reserva_baixa"] is True
    assert economia["recomendar_economia"] is True
    critica=avaliar_situacao_energetica(20,45,33,10,0,200)
    assert critica["situacao"] == "CRITICA"
    assert critica["situacao_critica"] is True
    assert critica["recomendar_economia"] is True
    baixa=avaliar_situacao_energetica(65,45,33,30,50,200)
    assert baixa["situacao"] == "RESERVA BAIXA"
    assert baixa["reserva_baixa"] is True
    assert baixa["recomendar_economia"] is False
    assert verificar_deficit_previsto(40,45) is True
    assert verificar_deficit_previsto(65,45) is False
    print("Testes das decisões: APROVADOS")

if __name__ == "__main__":
    testar_decisoes()

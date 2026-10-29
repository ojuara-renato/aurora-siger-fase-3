from codigo.dados import velocidades_vento, geracoes_eolicas, vento_previsto
from codigo.previsao import prever_geracao_eolica

def testar_previsao():
    previsao, inclinacao, intercepto = prever_geracao_eolica(velocidades_vento,geracoes_eolicas,vento_previsto)
    tolerancia=0.0001
    assert abs(inclinacao - 2.35) < tolerancia
    assert abs(intercepto - 0.50) < tolerancia
    assert abs(previsao - 26.35) < tolerancia
    print("Testes da regressão linear: APROVADOS")

if __name__ == "__main__":
    testar_previsao()

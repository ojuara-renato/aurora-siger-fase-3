from sklearn.linear_model import LinearRegression
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def prever_geracao_eolica(velocidades, geracoes, vento_previsto):
    X=[[velocidade] for velocidade in velocidades]
    modelo=LinearRegression()
    modelo.fit(X,geracoes)
    return modelo.predict([[vento_previsto]])[0], modelo.coef_[0], modelo.intercept_

def gerar_grafico_regressao(velocidades,geracoes,inclinacao,intercepto,vento_previsto):
    reta=[]
    for velocidade in velocidades:
        reta.append(inclinacao*velocidade+intercepto)
    previsao=inclinacao*vento_previsto+intercepto
    plt.scatter(velocidades,geracoes,color='blue',label='Dados históricos')
    plt.plot(velocidades,reta,color='red',label='Regressão linear')
    plt.scatter(vento_previsto,previsao,color='green',label='Previsão para 11 m/s')
    plt.xlabel('Velocidade do vento (m/s)')
    plt.ylabel('Geração eólica (kW)')
    plt.title('Aurora Siger - Previsão de geração eólica')
    plt.legend()
    plt.grid(True)
    plt.savefig('imagens/regressao_eolica.png', dpi=150, bbox_inches='tight')
    plt.close()

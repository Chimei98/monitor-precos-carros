import joblib
import pandas as pd

# importação de modelo já criado e treinado
print("[SYS] Iniciando modelo...")
pilot = joblib.load('modelo_preco.pkl')

# criacao de carro fictício
dados_novo_carro = {
    'quilometragem': [150000],
    'combustivel_Diesel': [1],
    'combustivel_Gasolina': [0],
    'caixa_Manual': [1]
}

# DataFrame para leitura pelo modelo
df_novo_carro = pd.DataFrame(dados_novo_carro)

print("[SYS] Carro fictício inicializado...")
print(df_novo_carro)

print('-'*50)
previsao = pilot.predict(df_novo_carro)

preco_estimado = previsao[0] # Pegar 1.º elemento, por conta de predict retornar um Array.
print(f"Preço estimado pelo carro é de : {preco_estimado:.2f} euros")
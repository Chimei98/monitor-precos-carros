import joblib
import pandas as pd

# importação de modelo já criado e treinado
print("[SYS] Iniciando modelo...")
pilot = joblib.load('modelo_preco.pkl')

dados_quilometros = input("Insira a quantidade de quilometros: ")
dados_combustivel = input("Insira o tipo de combustivel: ")
def determinarTipoCombustivel(dados_combustivel):
    if dados_combustivel == 'diesel':
        combustivel_Diesel = 1
        combustivel_Gasolina = 0
    else:
        combustivel_Gasolina = 1
        combustivel_Diesel = 0

    return combustivel_Diesel, combustivel_Gasolina

combustivel_Diesel, combustivel_Gasolina = determinarTipoCombustivel(dados_combustivel)

dados_caixa = input("Insire o tipo de caixa: ")
def determinarTipoCaixa(dados_caixa):
    if dados_caixa == 'manual':
        return 1
    else:
        return 0

# criacao de carro com base em dados dinamicos
dados_novo_carro = {
    'quilometragem': dados_quilometros,
    'combustivel_Diesel': combustivel_Diesel,
    'combustivel_Gasolina': combustivel_Gasolina,
    'caixa_Manual': determinarTipoCaixa(dados_caixa)
}

# DataFrame para leitura pelo modelo
df_novo_carro = pd.DataFrame([dados_novo_carro])

print("[SYS] Carro fictício inicializado...")
print(df_novo_carro)

print('-'*50)
previsao = pilot.predict(df_novo_carro)

preco_estimado = previsao[0] # Pegar 1.º elemento, por conta de predict retornar um Array.
print(f"Preço estimado pelo carro é de : {preco_estimado:.2f} euros")
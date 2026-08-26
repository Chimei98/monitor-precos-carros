import pandas as pd
import sqlite3
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

print("[PANDAS] Conectando ao banco de dados...")
print("[PANDAS] Version: " + pd.__version__)

# Conexão ao banco de dados
conexao = sqlite3.connect('carros-db.db')

# Extração de dados e Conversão para um Dataframe
df_carros = pd.read_sql_query("SELECT * FROM carros;", conexao)

# Fechar conexão após extração de dados
conexao.close()

# Configurações visuais
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# Leitura e Manipulação de dados
df_carros = df_carros.dropna(subset=['link', 'preco']) # remoção de dados corrompidos


# Exibição de dados
print("DADOS GERAIS")
print(df_carros) # Dataframe original
print('-'*100)

df_carros_preco_menor = df_carros.sort_values(by="preco", ascending=True) # Dataframe dos carros mais baratos
print("DADOS CARROS MAIS BARATOS")
print(df_carros_preco_menor.head())
print('-'*100)

df_carros_preco_maior = df_carros.sort_values(by="preco", ascending=False) # Dataframe dos carros mais caros
print("DADOS CARROS MAIS CAROS")
print(df_carros_preco_maior.head())

df_carros_dados = df_carros.describe() # Dataframe das estatísticas de cada carro
print('-'*100)
print("DADOS ESTATÍSTICOS")
print(df_carros_dados)

# Agrupamento de dados com base no tipo de combustível
print('-'*100)
fuelgroup_data = df_carros.groupby("combustivel")['preco'].mean() # Agrupamento da média de preços com base no tipo de combustível
print("DADOS AGRUPADOS")
print(fuelgroup_data)

# Transformação de coluna "combustivel" para indicadores binários para análise
print('-'*100)
df_binario = pd.get_dummies(df_carros, columns=['combustivel','caixa'], dtype=int)
print("DADOS EM BINÁRIO")
print(df_binario.head())
print('-'*100)
print(f"Tamanho de DF = {len(df_binario)}")

# Interquartis para prevenção de preços irreais
q1 = df_binario['preco'].quantile(0.25)
q3 = df_binario['preco'].quantile(0.75)
iqr = q3 - q1 # amplitude interquartil
lim_inf = q1 - (1.5 * iqr)
lim_sup = q3 + (1.5 * iqr)

df_binario = df_binario[(df_binario['preco'] >= lim_inf) & (df_binario['preco'] <= lim_sup)]
print('-'*100)
print(f"Tamanho de DF repartido = {len(df_binario)}")


# Matrizes de isolamento para análise preditiva de preço
print('-'*100)
df_x = df_binario.drop(columns=['id','nome','preco','link']) # variável de entrada
s_y = df_binario['preco'] # variável pretendida
print("DADOS SUPRIMIDOS")
print(df_x)
print('#'*100)
print(s_y)

# Análise Preditiva de preço
print('-'*100)
X_treino, X_teste, y_treino, y_teste = train_test_split(df_x, s_y, test_size=0.2, random_state=42) # 80% para treino // 20% para teste
print("DIMENSÕES DE DIVISÕES DOS DADOS (80/20")
print("#"*100)
print(f"Material de estudo (X_treino): {X_treino.shape}") # 6 carros para estudar. Cada um com 6 características (colunas) para estudo => 'quilometragem' e 'combustivel_TIPO'
print(f"Gabarido (y_treino): {y_treino.shape}") # 6 preços correspondentes => Série

print(f"Prova (X_teste): {X_teste.shape}")
print(f"Gabarito da prova (y_teste): {y_teste.shape}")

# Criação de modelo matemático para previsão de preços
modelo = LinearRegression()
# Treino de modelo
modelo.fit(X_treino, y_treino)
# Previsão
previsoes = modelo.predict(X_teste)
# Cálculo da margem de erro
erro = mean_absolute_error(y_teste, previsoes)
print("-"*100)
print("Margem de erro de modelo:")
print(f"    Aproximadamente: {erro} euros") # mais ou menos {erro} euros de diferença.

# Serialização de Modelo
joblib.dump(modelo, 'modelo_preco.pkl')



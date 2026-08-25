import pandas as pd
import sqlite3

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
df_binario = pd.get_dummies(df_carros, columns=['combustivel'], dtype=int)
print("DADOS EM BINÁRIO")
print(df_binario.head())


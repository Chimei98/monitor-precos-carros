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
print(df_carros) # Dataframe original
print('-'*200)

df_carros_preco_menor = df_carros.sort_values(by="preco", ascending=True) # Dataframe dos carros mais baratos
print(df_carros_preco_menor.head())
print('-'*200)

df_carros_preco_maior = df_carros.sort_values(by="preco", ascending=False) # Dataframe dos carros mais caros
print(df_carros_preco_maior.head())

df_carros_dados = df_carros.describe() # Dataframe das estatísticas de cada carro
print('-'*200)
print("DADOS ESTATÍSTICOS")
print(df_carros_dados)





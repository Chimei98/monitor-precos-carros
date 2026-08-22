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

# Exibição de dados => 5 dados
print('-'*100)
print("DADOS DA TABELA 'CARROS' ")
print(df_carros.head())


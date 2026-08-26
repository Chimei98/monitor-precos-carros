# Automotive Market Data Extractor
Pipeline de extração, tratamento e análise de dados de classificados automotivos, desenvolvido em Python. O projeto utiliza técnicas de análise de dados e modelagem preditiva para auxiliar na identificação das melhores opções de veículos usados com base nos critérios definidos pelo utilizador.

## Visão Geral Técnica
A versão atual do sistema foca em estabilidade, resiliência na raspagem de dados e filtragem de oportunidades em tempo de execução. O motor de busca mapeia atributos semânticos do DOM (`data-parameter`) e extrai links absolutos manipulando as propriedades nativas das tags HTML (`href`).

Principais características arquiteturais desta fase:

### Pipeline ETL (Extract, Transform, Load)
* **Roteamento Dinâmico de Requisições:** Construção em tempo de execução das URLs alvo com base em parâmetros de entrada (marca e modelo).
* **Questionamento ao Usuário:** Implementação de limites paramétricos de preço e quilometragem definidos pelo usuário.
* **Bypass de Proteção HTTP:** Mascaramento de requisições através da injeção de `Headers` e `User-Agent` específicos, mitigando bloqueios primários no servidor de origem (evasão de erros 403/429).


### Machine Learning

O projeto evoluiu para além da extração, incorporando um módulo de Inteligência Artificial para a precificação preditiva de veículos, aplicando rigor estatístico e álgebra linear na análise de mercado:

* **Atribuições :** Uso de funções como `.drop()` para a supressão de colunas indesejáveis para o cálculo preditivo de preço. Criação de vetores matriciais, `df_x`, a partir de características gerais (tipo de combustíveis), transformando em indicadores binários; Vetor unidimensional `s_y` utilizado para armazenamento dos preços almejados na previsão.
* **Particionamento Estrutural:** Segregação do banco de dados em matrizes de características independentes (X) e vetor alvo dependente (y), com retenção de 20% da amostra isolada em um ambiente de teste empírico para mitigação técnica de *"ruído"* na análise.
* **Modelo Preditivo (Regressão Linear Múltipla):** O núcleo preditivo foi modelado no Scikit-Learn. O algoritmo supervisionado projeta um modelo matemático para inferir preços, otimizando computacionalmente a seguinte equação algébrica:
  
$$ y = w_1x_1 + w_2x_2 + \dots + w_nx_n + b $$
  
*(Onde `y` representa o preço final estimado, `x` denota os atributos numéricos isolados do veículo, `w` reflete os pesos dinâmicos ajustados pela máquina através da minimização do erro quadrático, e `b` atua como o intercepto escalar).*

* **Tratamento de Erro:** A margem de desvio do modelo perante dados desconhecidos (conjunto de teste) é auferida matematicamente pela métrica de Erro Absoluto Médio (dito, MAE):
  
$$ MAE = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i| $$
  
*(Onde `yᵢ` estabelece o gabarito objetivo do mercado e `ŷᵢ` reflete a inferência preditiva consolidada, expressando o desvio linear residual direto em Euros).*

---

## Stack Tecnológica

* **Python**
* **BeautifulSoup4** (Parsing e navegação no DOM)
* **Requests** (Comunicação de rede e manipulação do protocolo HTTP)
* **SQLAlchemy** (Object-Relational Mapping para a modelagem de dados)
* **SQLite3** (Motor de banco de dados leve para desenvolvimento local)
* **Pandas** (Estruturação de DataFrames em memória, limpeza de dados nulos e análise estatística descritiva)
* **Scikit-Learn** (Construção do motor de inteligência artificial e validação algébrica do modelo de regressão)
---

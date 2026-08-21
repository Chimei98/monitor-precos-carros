# Automotive Market Data Extractor

Um pipeline dinâmico de extração de dados desenvolvido em Python, projetado para capturar, estruturar e validar informações de classificados automotivos. Este projeto atua como o módulo de ingestão de dados fundamental para um futuro sistema de análise preditiva de preços.

## Visão Geral Técnica

A versão atual do sistema foca em estabilidade, resiliência na raspagem de dados e filtragem de oportunidades em tempo de execução. O motor de busca mapeia atributos semânticos do DOM (`data-parameter`) e extrai links absolutos manipulando as propriedades nativas das tags HTML (`href`).
Principais características arquiteturais desta fase:
* **Roteamento Dinâmico de Requisições:** Construção em tempo de execução das URLs alvo com base em parâmetros de entrada (marca e modelo).
* **Sistema de Thresholds (Gatilhos):** Implementação de limites paramétricos de preço e quilometragem definidos pelo usuário, utilizando avaliação de curto-circuito (short-circuit evaluation) para descartar dados fora do escopo antes do processamento.
* **Bypass de Proteção HTTP:** Mascaramento de requisições através da injeção de `Headers` e `User-Agent` específicos, mitigando bloqueios primários no servidor de origem (evasão de erros 403/429).

## Stack Tecnológica

* **Python**
* **BeautifulSoup4** (Parsing e navegação no DOM)
* **Requests** (Comunicação de rede e manipulação do protocolo HTTP)
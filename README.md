# Automotive Market Data Extractor

Um pipeline dinâmico de extração de dados desenvolvido em Python, projetado para capturar, estruturar e validar informações de classificados automotivos. Este projeto atua como o módulo de ingestão de dados fundamental para um futuro sistema de análise preditiva de preços.

## Visão Geral Técnica

A versão atual do sistema foca em estabilidade e resiliência na raspagem de dados. Em vez de depender de classes CSS voláteis (frequentemente alteradas por frameworks de frontend), o motor de busca mapeia atributos semânticos do DOM, garantindo alta disponibilidade da extração.

Principais características arquiteturais desta fase:
* **Roteamento Dinâmico de Requisições:** Construção em tempo de execução das URLs alvo com base em parâmetros de entrada (marca e modelo).
* **Tolerância a Falhas na Extração:** Implementação de validação rigorosa de dados nulos (null-safety) utilizando operadores ternários, prevenindo interrupções de execução (runtime exceptions) causadas por anomalias ou dados ausentes na árvore do DOM.
* **Bypass de Proteção HTTP:** Mascaramento de requisições através da injeção de `Headers` e `User-Agent` específicos, mitigando bloqueios primários no servidor de origem (evasão de erros 403/429).

## Stack Tecnológica

* **Python 3.x**
* **BeautifulSoup4** (Parsing e navegação no DOM)
* **Requests** (Comunicação de rede e manipulação do protocolo HTTP)
from bs4 import BeautifulSoup
import requests
from database import _Sessao, Carro
from sqlalchemy.exc import IntegrityError

print("Bem vindo ao Sistema de Busca de Carros")
print("-" * 50)

def obter_parametros_busca():
    marca = input("Informe o nome da marca: ").strip()
    modelo = input("Informe o nome do modelo: ").strip()

    preco_max = input("Informe o preço máximo que deseja: ")
    goal = int(preco_max) if preco_max.isdigit() and int(preco_max) > 0 else None

    km_max = input("Informe a quantidade de km máxima: ")
    goal_km = int(km_max) if km_max.isdigit() and int(km_max) > 0 else None

    return marca, modelo, goal, goal_km

def buscar_anuncios(marca, modelo):
    page_to_scrape = f"https://www.standvirtual.com/carros/{marca}/{modelo}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

    print("-" * 50)
    print("Acessando servidor...")
    resposta = requests.get(page_to_scrape, headers=headers)

    if resposta.status_code == 200:
        print("Conexão bem sucedida! Extraindo dados...")
        print("*" * 50)
        soup = BeautifulSoup(resposta.text, 'html.parser')
        carros = soup.find_all("article", {"class": "ooa-zet1mn e1srzcph1"})
        return carros
    else:
        print("Falha na conexão.")
        return []

def extrair_dados_carro(carro, goal, goal_km):
    nome = carro.find("h2", {"class": "e123dwbo0 ooa-ezpr21"})
    preco = carro.find("h3", {"class": "eg88ra81 ooa-3ewd90"})
    quilometragem = carro.find("dd", {"data-parameter": "mileage"})
    fuel = carro.find("dd", {"data-parameter": "fuel_type"})
    gearbox = carro.find("dd", {"data-parameter": "gearbox"})
    link = carro.find("a", {"data-nextlink": "false"})

    nome_texto = nome.text if nome else "Nome não informado."
    link_url = link.get("href") if link else "Link não encontrado."

    preco_texto = preco.text if preco else "Preço não informado."
    preco_limpo = 0
    if preco_texto != "Preço não informado.":
        preco_limpo = int(preco_texto.replace("EUR", "").replace(" ", "").strip())

    quilometragem_texto = quilometragem.text if quilometragem else "Quilometragem não informada."
    quilometragem_limpa = 0
    if quilometragem_texto != "Quilometragem não informada.":
        quilometragem_limpa = int(quilometragem_texto.replace("km", "").replace(" ", "").strip())

    if (goal is not None and preco_limpo > goal) or (goal_km is not None and quilometragem_limpa > goal_km):
        return None

    fuel_texto = fuel.text if fuel else "Combustível não informado."
    gearbox_texto = gearbox.text if gearbox else "Caixa não informada."

    return {
        "nome": nome_texto,
        "preco": preco_limpo,
        "quilometragem": quilometragem_limpa,
        "combustivel": fuel_texto,
        "caixa": gearbox_texto,
        "link": link_url
    }

marca, modelo, goal, goal_km = obter_parametros_busca()

lista_artigos_html = buscar_anuncios(marca, modelo)

if lista_artigos_html:
    with _Sessao() as sessao:
        for artigo in lista_artigos_html:

            dados = extrair_dados_carro(artigo, goal, goal_km)

            if dados is None:
                continue

            try:
                sessao.add(Carro(
                    nome=dados["nome"],
                    preco=dados["preco"],
                    quilometragem=dados["quilometragem"],
                    combustivel=dados["combustivel"],
                    caixa=dados["caixa"],
                    link=dados["link"]
                ))
                sessao.commit()
                print(f"SALVO: {dados['nome']}")

            except IntegrityError:
                sessao.rollback()
                print(f"DUPLICADO: {dados['nome']}")
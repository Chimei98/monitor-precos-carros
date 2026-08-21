from asyncio.windows_events import NULL

from bs4 import BeautifulSoup
import requests

print("Bem vindo ao Sistema de Busca de Carros")
print("-"*50)

# Asking user about his preferences
marca = input("Informe o nome da marca: ").strip()
modelo = input("Informe o nome do modelo: ").strip()

preco_max = input("Informe o preço máximo que deseja: ")
goal = int(preco_max) if preco_max.isdigit() and int(preco_max) > 0 else None

km_max = input("Informe a quantidade de km máxima: ")
goal_km = int(km_max) if km_max.isdigit() and int(km_max) > 0 else None

# Getting the url
page_to_scrape = f"https://www.standvirtual.com/carros/{marca}/{modelo}"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

print("-"*50)
print("Acessando servidor...")
resposta = requests.get(page_to_scrape, headers=headers)

if resposta.status_code == 200:
    print("Conexão bem sucedida! Extraindo dados...")
    print("*"*50)

    soup = BeautifulSoup(resposta.text, 'html.parser')


    # Padrão - todos os anúncios estão contidos em 'articles' com uma classe geral
    carros = soup.find_all("article", {"class": "ooa-zet1mn e1srzcph1"})

    for carro in carros:
        nome = carro.find("h2", {"class": "e123dwbo0 ooa-ezpr21"}) # nome do carro
        preco = carro.find("h3", {"class": "eg88ra81 ooa-3ewd90"}) # preço do carro
        quilometragem = carro.find("dd", {"data-parameter": "mileage"}) # quilometragem
        fuel = carro.find("dd", {"data-parameter": "fuel_type"}) # tipo de combustível
        gearbox = carro.find("dd", {"data-parameter": "gearbox"}) # tipo de caixa
        link = carro.find("a", {"data-nextlink": "false"})

        # Extração de texto para segurança de dados
        nome_texto = nome.text if nome else "Nome não informado."
        link_url = link.get("href") if link else "Link não encontrado."

        # Casting de dados STR => INT de maneira segura.
        preco_texto = preco.text if preco else "Preço não informado."
        preco_limpo = 0
        if preco_texto != "Preço não informado.":
            preco_limpo = int(preco_texto.replace("EUR", "").replace(" ", "").strip())

        quilometragem_texto = quilometragem.text if quilometragem else "Quilometragem não informada."
        if quilometragem_texto != "Quilometragem não informada.":
            quilometragem_limpa = int(quilometragem_texto.replace("km", "").replace(" ", "").strip())


        # Filtro condicional
        if (goal is not None and preco_limpo > goal) or (goal_km is not None and quilometragem_limpa > goal_km):
            continue

        # Continuação da extração de dados.
        fuel_texto = fuel.text if fuel else "Combustível não informado."
        gearbox_texto = gearbox.text if gearbox else "Caixa não informada."

        print(f"Carro: {nome_texto} | Preço: {preco_texto} | Quilometragem: {quilometragem_texto} | Combustível: {fuel_texto} | Caixa: {gearbox_texto} | Link: {link_url}")
        print("-"*100)
else:
    print("Falha na conexão.")



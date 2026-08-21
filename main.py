from asyncio.windows_events import NULL

from bs4 import BeautifulSoup
import requests

print("Bem vindo ao Sistema de Busca de Carros")
print("-"*50)
marca = input("Informe o nome da marca: ")
modelo = input("Informe o nome da modelo: ")

# Getting the url
page_to_scrape = f"https://www.standvirtual.com/carros/{marca}/{modelo}"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

print("-"*50)
print("Acessando servidor...")
resposta = requests.get(page_to_scrape, headers=headers)

if resposta.status_code == 200:



    print("Conexão bem sucedida! Extraindo dados")
    print("*"*50)

    soup = BeautifulSoup(resposta.text, 'html.parser')

    carros = soup.find_all("article", {"class": "ooa-zet1mn e1srzcph1"})

    for carro in carros:
        nome = carro.find("h2", {"class": "e123dwbo0 ooa-ezpr21"})
        preco = carro.find("h3", {"class": "eg88ra81 ooa-3ewd90"})
        quilometragem = carro.find("dd", {"data-parameter": "mileage"})
        fuel = carro.find("dd", {"data-parameter": "fuel_type"})
        gearbox = carro.find("dd", {"data-parameter": "gearbox"})

        # Extração de texto para segurança de dados
        nome_texto = nome.text if nome else "Nome não informado."
        preco_texto = preco.text if preco else "Preço não informado."
        quilometragem_texto = quilometragem.text if quilometragem else "Quilometragem não informada."
        fuel_texto = fuel.text if fuel else "Combustível não informado."
        gearbox_texto = gearbox.text if gearbox else "Caixa não informada."

        print(f"Carro: {nome_texto} | Preço: {preco_texto} | Quilometragem: {quilometragem_texto} | Combustível: {fuel_texto} | Caixa: {gearbox_texto}")
        print("-"*50)
else:
    print("Falha na conexão.")



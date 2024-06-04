import json
import requests
import os

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
dir_restaurantes = 'restaurantes'
dados_restaurante = {}

def captura_restaurantes(): 
    response = requests.get(url)

    if response.status_code == 200: 
        dados_json = response.json()
        for item in dados_json: 
            nome_restaurante = item['Company']
            if nome_restaurante not in dados_restaurante: 
                dados_restaurante[nome_restaurante] = []
            
            dados_restaurante[nome_restaurante].append({
                "item": item['Item'],
                "price": item['price'],
                "description": item['description']
            })
    else: 
        print('f Erro ao obter dados do response: {response}')


def gera_diretorio_restaurantes(): 
    try:
        os.makedirs('./' + dir_restaurantes)
    except: 
        pass

def escreve_arquivos(): 
    for nome_restaurante, dados in dados_restaurante.items(): 
        nome_arquivo = f'{nome_restaurante}.json'
        with open(dir_restaurantes + '/' + nome_arquivo, 'w') as arquivo_restaurante: 
            json.dump(dados, arquivo_restaurante, indent=4)

def main(): 
    gera_diretorio_restaurantes()
    captura_restaurantes()
    escreve_arquivos()

if __name__ == '__main__': 
    main()
        
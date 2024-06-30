#Andre Alves de Lima 11630-067
#Luiz Felipe Alves da Silva 11634-060
#Laercio Alexandre de Oliveira 11630-135
#Nicolas Galha Lemes 11630-065

#Criando o ambiente virtual para o exercico no terminal

#python -m venv ambientevirtual1 (criar ambiente virtual no vscode)
#.\ambientevirtual1\Scripts\activate (ativar o ambiente virtual)
#pip install requests (instalando a biblioteca de requisicao)

import requests #Importando a biblioteca de requisição

squad = {
    "Andre Alves de Lima" : "11630-067",
    "Luiz Felipe Alves da Silva" : "11634-060",
    "Laercio Alexandre de Oliveira" : "11630-135",
    "Nicolas Galha Lemes" : "11630-065"
    } # Dicionario com o nome dos integrantes do squad 6 e seus CEPs

resultado = {} #um novo dicionario que será armazenado a cidade dos integrantes após o request


#Loop para pesquisar o CEP de cada integrante e adicionar no dicionario novo sua cidade
for nome, cep in squad.items(): 
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/') #requisicao para pesquisar o cep
    if response.status_code == 200: #se voltar o status 200, quer dizer que o cep existe e a busca teve exito
        data = response.json() #variavel que recebe a lista de busca do cep
        cidade = data.get("localidade") #get que pesquisa a "localidade" (cidade) do integrante pesquisado, dentro da lista
        resultado[nome] = cidade #dicionario que recebe o nome e a cidade do integrante buscado

for nome, cidade in resultado.items(): #Loop para imprimir o dicionario de nome e cidade
    print(f'A cidade do integrante {nome}, é {cidade}')

with open ("requirements.txt", "w") as f: #gerar o arquivo requirements.txt de forma automatica
    f.write("requests\n")

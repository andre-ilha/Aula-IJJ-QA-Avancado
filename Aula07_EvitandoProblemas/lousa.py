import requests

cep = input("Qual seu CEP: ")

response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

data = response.json()

print(f'O logradouro dessa chamada é {data['logradouro']}')


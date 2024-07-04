#1. O squad deverá criar usuário no seguinte endpoint https://desafiopython.jogajuntoinstituto.org/api/users/.
#2. Em seguida, deve fazer login com o usuário criado http://desafiopython.jogajuntoinstituto.org/api/users/login/.
#3. Deve salvar o Json que receber de resposta.

import requests
from faker import Faker
import json

fake = Faker('pt_BR')

def criarpersona() -> dict:

    data = {
        "username" : fake.user_name(),
        "email" : fake.email(),
        "password" : fake.password(),
        "phone" : fake.phone_number(),
        "address" : fake.address(),
        "cpf" : fake.cpf()
    }
    return data

usuario = criarpersona()

def salvar_txt(logjson, conteudo):
    with open(logjson, 'a') as arquivo:
        arquivo.write(conteudo + '\n')
    print(f'Dados salvo em {logjson}.')

def criaruserapi():
    endpoint_criaruser = "https://desafiopython.jogajuntoinstituto.org/api/users/"
    response = requests.post(endpoint_criaruser, json=usuario)

    if response.status_code == 201:
        print('Usuário criado com sucesso!')
        print(response.json())
        salvar_txt('reposta_api.txt', json.dumps(response.json(), indent=4))
        return True
    else:
        print('Falha ao criar usuário.')
        print('Status code: ', response.status_code)
        print('Resposta: ', response.json())
        salvar_txt('reposta_api.txt', json.dumps(response.json(), indent=4))
        return False

def loginuserapi():
    endpoint_login = 'http://desafiopython.jogajuntoinstituto.org/api/users/login/'
    login_data = {
        'email': usuario["email"],
        'password':usuario["password"]
    }

    response = requests.post(endpoint_login, json=login_data)

    if response.status_code == 200:
        print('Login realizado com sucesso!')
        print(response.json())
        salvar_txt('reposta_api.txt', json.dumps(response.json(), indent=4))
    else:
        print('Falha ao realizar login.')
        print('Status code:', response.status_code)
        print('Resposta:', response.json())
        salvar_txt('reposta_api.txt', json.dumps(response.json(), indent=4))

if criaruserapi():
     loginuserapi()

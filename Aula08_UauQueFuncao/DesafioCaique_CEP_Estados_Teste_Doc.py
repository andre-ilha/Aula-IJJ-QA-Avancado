import requests

estado_desconto = ["AL", "BA", "CE", "MA", "PE", "PI", "RN", "SE", "AC", "AP", "AM", "PA", "RO", "RR", "TO"]

#cep = input("Favor digitar seu CEP: ")

def verificaestado(estado):
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    data = response.json()
    if 'erro' not in data:
        estado = data["uf"]
        return estado in estado_desconto
    return False

#if verificaestado(cep):
#    print("O CEP inserido é elegível para frete grátis.")
#else:
#    print("O CEP inserido não é elegível para frete grátis.")

#Faça pra mim uma lista de 15 Ceps aleatórios de qualquer lugar do brasil para eu efetuar testes.

#ChatGPT
#Claro! Aqui está uma lista de 15 CEPs aleatórios de diferentes regiões do Brasil para que você possa realizar os testes:

cep_teste = [
    '01001-000', #São Paulo, SP (Sudeste)
    '20040-002', #Rio de Janeiro, RJ (Sudeste)
    '60060-080', #Fortaleza, CE (Nordeste)
    "30140-071", #Belo Horizonte, MG (Sudeste)
    '40020-000', #Salvador, BA (Nordeste)
    '72000-000', #Brasília, DF (Centro-Oeste)
    '78048-000', #Cuiabá, MT (Centro-Oeste)
    '11630-346', #Ilhabela, SP (Sudeste)
    '69010-060', #Manaus, AM (Norte)
    '09051-160', #Santo André, SP (Sudeste)
    '75000-000', #Anápolis, GO (Centro-Oeste)
    '69900-060', #Rio Branco, AC (Norte)
    '87020-025', #Maringá, PR (Sul)
    '89890-000', #Xanxerê, SC (Sul)
    '90000-000'  #Porto Alegre, RS (Sul)
]

for cep in cep_teste:
    elegivel = verificaestado(cep)
    print(f'CEP: {cep}, Elegivel para frete grátis: {elegivel}')

#Teste de Sucesso:
#Dado: CEP Elegivel (Norte ou Nordeste)
#Resultado Esperado: CEP Elegível
#Resultado Obtido: CEP Elegível
#Status: Passou

#Teste de Falha:
#Dado: CEP Não Elegível (Sul, Sudeste, Centro-Oeste)
#Resultado Esperado: CEP Não Elegível
#Resultado Obtido: CEP Não Elegível
#Status: Passou


#CEP: 01001-000, Esperado: Não Elegível, Resultado: Não Elegível
#CEP: 20040-002, Esperado: Não Elegível, Resultado: Não Elegível
#CEP: 60060-080, Esperado: Elegível, Resultado: Elegível
#CEP: 30140-071, Esperado: Não Elegível, Resultado: Não Elegível
#CEP: 40020-000, Esperado: Elegível, Resultado: Elegível
#CEP: 72000-000, Esperado: Não Elegível, Resultado: Não Elegível
#CEP: 78048-000, Esperado: Não Elegível, Resultado: Não Elegível
#CEP: 11630-346, Esperado: Não Elegível, Resultado: Não Elegível
#CEP: 69010-060, Esperado: Elegível, Resultado: Elegível
#CEP: 09051-160, Esperado: Não Elegível, Resultado: Não Elegível
#CEP: 75000-000, Esperado: Não Elegível, Resultado: Não Elegível
#CEP: 69900-060, Esperado: Elegível, Resultado: Elegível
#CEP: 87020-025, Esperado: Não Elegível, Resultado: Não Elegível
#CEP: 89890-000, Esperado: Não Elegível, Resultado: Não Elegível
#CEP: 90000-000, Esperado: Não Elegível, Resultado: Não Elegível
#A partir de uma requisição na API, pesquisando pelo CEP, verificar se o estado da pesquisa fica nas regiões norte e nordeste, 
# para  assim verificar se o estado está incluso na política de frete grátis

#Região Centro-Oeste: Distrito Federal, Goiás, Mato Grosso, Mato Grosso do Sul
#Região Nordeste: Alagoas, Bahia, Ceará, Maranhão, Pernambuco, Piauí, Rio Grande do Norte, Sergipe
#Região Norte: Acre, Amapá, Amazonas, Pará, Rondônia, Roraima, Tocantis
#Região Sudeste: Espírito Santo, Minas Gerais, Rio de Janeiro, São Paulo
#Região Sul: Paraná, Rio Grande do Sul, Santa Catarina

#Importanto biblioteca de requisição
import requests

#Lista de estados inclusos na política de frete grátis
estado_desconto = ["AL", "BA", "CE", "MA", "PE", "PI", "RN", "SE", "AC", "AP", "AM", "PA", "RO", "RR", "TO"]

#input de usuário, digitando seu CEP
cep = input("Favor digitar seu CEP: ")

#Função para verificar se o CEP digitado esta dentro da lista de estados com frete grátis
def verificaestado(estado):
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    data = response.json()
    estado = data["uf"]
    return estado in estado_desconto

#Impressão do resultado
if verificaestado(cep):
    print("O CEP inserido é elegível para frete grátis.")
else:
    print("O CEP inserido não é elegível para frete grátis.")

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



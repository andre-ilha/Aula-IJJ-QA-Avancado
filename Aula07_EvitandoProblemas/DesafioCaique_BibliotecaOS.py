import os #importante a biblioteca do sistema operacional

#Criando uma lista de dados ficticia

dados = [
    {'nome': 'Andre', 'idade' : 39, 'cidade' : 'Ilhabela'},
    {'nome': 'Alice', 'idade' : 31, 'cidade' : 'Sao Sebastiao'},
    {'nome': 'Gustavo', 'idade' : 38, 'cidade' : 'Sao Bernardo do Campo'},
    {'nome': 'Gabriel', 'idade' : 40, 'cidade' : 'Florianopolis'}
]

#Diretório onde o arquivo será salvo
diretorio = '.\Aula-IJJ-QA-Avancado\Aula07_EvitandoProblemas\DesafioCaique_BibliotecaOS'

#Cria a pasta se ela não exitir
if not os.path.exists(diretorio):
    os.makedirs(diretorio)

#Caminho do arquivo
caminho_arquivo = os.path.join(diretorio, "DesafioCaique_BibliotecaOS.txt")

#Escreve os dados no arquivo
with open(caminho_arquivo, "w") as arquivo:
    for pessoa in dados:
        arquivo.write(f'Nome: {pessoa["nome"]}, Idade: {pessoa['idade']}, Cidade: {pessoa['cidade']}\n')

print(f'Arquivo salvo em: {caminho_arquivo}')
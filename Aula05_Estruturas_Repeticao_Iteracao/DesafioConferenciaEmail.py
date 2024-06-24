
email_usuario = input("Por favor, insira seu e-mail: ")

#Caso de Teste BDD

#Cenário de Sucesso:
#Dado que o usuário insere um e-mail
#Quando o e-mail contem "@jogajuntoinstituto.org"
#Então o sistema deve indicar e-mail válido.

#Cenário de Falha:
#Dado que o usuário insere um e-mail
#Quando o e-mail não contem "@jogajuntoinstituto.org"
#Então o sistema deve indicar e-mail inválido.

while "@jogajuntoinstituto.org" not in email_usuario:  
    print("Email inválido. O e-mail deve conter '@jogajuntoinstituto.org'.")
    email_usuario = input("Por favor, insira seu e-mail novamente: ")

print("Email válido.")

#Documentação dos Resultados dos Testes

#Teste de Sucesso:

#Dado: Email usuario@jogajuntoinstituto.org
#Resultado Esperado: Email válido
#Resultado Obtido: Email válido
#Status: Passou
#Teste de Falha:

#Dado: Email usuario@gmail.com
#Resultado Esperado: Email inválido
#Resultado Obtido: Email inválido
#Status: Passou
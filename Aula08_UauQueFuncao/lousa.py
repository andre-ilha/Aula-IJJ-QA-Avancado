#Funçao e Procedimento

#Função:
#Definição: Uma função é um bloco de código que realiza uma tarefa específica e retorna um valor.
#Uso: Geralmente usada para calcular e retornar um resultado.

#Procedura (ou Procedimento):
#Definição: Uma procedura é um bloco de código que realiza uma tarefa específica mas não retorna um valor (ou retorna None implicitamente).
#Uso: Geralmente usada para realizar ações como imprimir algo na tela, modificar um arquivo, etc., sem a necessidade de um valor de retorno.

#Procedimento
def saudacao(nome):
    print(f"Olá {nome}, essa é uma função")

saudacao('Dehco')

#Função
#def soma (a, b):
#    resultado = a + b

#    return resultado

def soma (a:int, b:int) -> int: #não é obrigatório, mas é boa pratica
    resultado = a + b

    return resultado

resultado_soma  = soma(1 , 3)
if resultado_soma < 3:
    print(resultado_soma)
else:
    print("não")

def parimpar(matricula):
    if matricula % 2 == 0:
        return('VOCÊ ESTÁ NO TIME AZUL')
    else:
        return('VOCÊ ESTÁ NO TIME AMARELO')

numeros_matricula = []

for i in range(5):
    numero = int(input(f'Digite o numero de matrícula: '))
    numeros_matricula.append(numero)

for numero in numeros_matricula:
    resultado = parimpar(numero)
    print(f'Número de matrícula {numero}: {resultado}')
    
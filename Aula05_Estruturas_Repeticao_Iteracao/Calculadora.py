operacao = input("Digite a operação (soma, subtracao, multiplicacao, divisao): ").lower()
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

match operacao:
    case 'soma':
        resultado = num1 + num2
    case 'subtracao':
        resultado = num1 - num2
    case 'multiplicacao':
        resultado = num1 * num2
    case 'divisao':
        resultado = num1 / num2        
    case _:
        resultado = 'Operação inválida'


print(f"Resultado da {operacao}: {resultado}")
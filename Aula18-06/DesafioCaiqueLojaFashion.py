valorcompra = float(input("Informe o valor de sua compra em Reais: R$ "))

if valorcompra < 250:
    print('POXA, FALTA POUCO PARA VOCÊ GANHAR 10% DE DESCONTO EM SUA COMPRA.')

elif valorcompra > 500:
    print('PARABÉNS. VOCÊ GANHOU SUPER DESCONTO DE 30%')
    valordesconto = valorcompra*0.7
    print(f"O VALOR A SER PAGO COM DESCONTO AGORA É DE R$ {valordesconto:,.2f}")

else:
    print('PARABÉNS. VOCÊ GANHOU 10% DE DESCONTO, MAS PODE GANHAR 30% SE SUA COMPRA FOR ACIMA DE R$500,00')
    valordesconto = valorcompra*0.9
    print(f"O VALOR A SER PAGO COM DESCONTO AGORA É DE R$ {valordesconto:,.2f}")

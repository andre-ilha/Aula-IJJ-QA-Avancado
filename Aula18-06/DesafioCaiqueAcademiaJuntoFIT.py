print("VOCÊ ESTÁ PARTICIPANDO DA NOSSA PROMO TREINA JUNTO")
falta = input("Você veio no treino passado? Escreva com sim ou não: ")

if falta == "sim":
    frequencia = int(input("Digite o número de dias seguidos que você veio a academia: "))
    if frequencia >= 21:
        print('UHUU. AGORA VOCÊ PODE PRESENTEAR UM AMIGO OU AMIGA PARA TREINAR COM VOCÊ')

    else:
        print('Bom Treino')

else:
    print('QUE BOM VER VOCÊ DE VOLTA. A PARTIR DE AGORA INICIAMOS MAIS UMA CONTAGEM DE 21 DIAS PARA A PROMO TREINA JUNTO.')

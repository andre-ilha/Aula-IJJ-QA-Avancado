time = input("Digite seu time: ")

#if time == 'Corinthians':
#    print("Você é um Timão!")
#elif time == "Bahia":               #Pode repetir o elif sempre que quiser colocar mais condições;
#    print("Você é Esquadrão")
#else:
#    print("Você não é Timão!")



match time:
    case "Corinthians":
        print("Você é um Timão!")
    case "Bahia":
        print("Você é Esquadrão!")
    case "Gremio":
        print("Você é um Imortal!")
    case _:
        print("Quem não é, não se mete!")
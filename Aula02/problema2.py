velMax = int(input("Digite o valor da velocidade máxima: "))
vel = int(input("Digite o valor da velocidade registrada: "))

if vel <= velMax:
    print("Sem infração")
elif vel <= velMax*1.2:
    print("Infração Média")
elif vel <= velMax*1.5:
    print("Infração Grave")
else:
    print("Infração gravíssima")

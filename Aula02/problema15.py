arremesso = []
pontos = 0
arremesso.append(float(input("Digite o primeiro arremesso: ")))
arremesso.append(float(input("Digite o segundo arremesso: ")))
arremesso.append(float(input("Digite o terceiro arremesso: ")))

for a in arremesso:
    if a == -1:
        pontos += 1
    else:
        if a > 7.24:
            pontos += 3
        else:
            pontos += 2

print(f"Pontuação: {pontos}")

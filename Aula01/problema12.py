valPedro = float(input("Digite o valor que o Pedro apostou: "))
valJoao = float(input("Digite o valor que o João apostou: "))
valMarcela = float(input("Digite o valor que a Marcela apostou: "))
premio = float(input("Digite o valor do prêmio: "))

somaVal = valJoao+valMarcela+valPedro

premioPedro = valPedro/somaVal * premio
premioJoao = valJoao/somaVal * premio
premioMarcela = valMarcela/somaVal * premio

print(f"Prêmio do Pedro: {premioPedro:.2f}")
print(f"Prêmio do João: {premioJoao:.2f}")
print(f"Prêmio da Marcela: {premioMarcela:.2f}")
salario = float(input("Digite o valor do salário: "))

if salario <= 280:
    aumento = salario * .2
elif salario <= 700:
    aumento = salario * .15
elif salario <= 1500:
    aumento = salario * .1
else:
    aumento = salario *.05

print(f"Valor do aumento: {aumento:.2f}")
print(f"Novo salário: {(salario+aumento):.2f}")

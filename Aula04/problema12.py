salario_carlos = float(input("Digite o salário do Carlos: "))
salario_joao = salario_carlos/3
rend_poup = float(input("Digite o rendimento da poupança(%): "))/100
rend_rf = float(input("Digite o rendimento do fundo de renda fixa(%): "))/100

meses = 0
while salario_joao<salario_carlos:
    salario_carlos *= 1 + rend_poup
    salario_joao *= 1 + rend_rf
    meses += 1

print(f"Meses: {meses}")

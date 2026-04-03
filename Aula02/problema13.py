valor_hora = float(input("Digite o valor da hora de trabalho: "))
hora_trab = int(input("Digite a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * hora_trab
valor_INSS = salario_bruto * 0.1
valor_FGTS = salario_bruto * 0.11

if salario_bruto <= 900:
    valor_IR = 0
elif salario_bruto <= 1500:
    valor_IR = salario_bruto * 0.05
elif salario_bruto <= 2500:
    valor_IR = salario_bruto * 0.1
else:
    valor_IR = salario_bruto * 0.2

print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"IR: R$ {valor_IR:.2f}")
print(f"INSS: R$ {valor_INSS:.2f}")
print(f"FGTS: R$ {valor_FGTS:.2f}")
print(f"Total de descontos: R$ {(valor_IR + valor_INSS):.2f}")
print(f"Salário Líquido: R$ {salario_bruto - (valor_IR + valor_INSS):.2f}")

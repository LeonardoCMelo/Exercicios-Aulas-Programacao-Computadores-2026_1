custoFabrica = float(input("Digite o custo de fábrica: "))

if custoFabrica <= 12000:
    comissao = custoFabrica * 0.05
    imposto = 0
elif custoFabrica <= 25000:
    comissao = custoFabrica * 0.10
    imposto = custoFabrica * 0.15
else:
    comissao = custoFabrica * .15
    imposto = custoFabrica * .20

print(f"Custo total: {(custoFabrica+comissao+imposto):.2f}")

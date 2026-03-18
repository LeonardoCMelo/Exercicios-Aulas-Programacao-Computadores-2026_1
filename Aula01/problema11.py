vp = float(input("Digite o valor do investimento inicial: "))
i = float(input("Digite a taxa de juros anual: "))
n = float(input("Digite o período do investimento em anos: "))

vf =  vp*(1+(i *0.01))**n

print(f"Valor futuro: {vf:.2f}")
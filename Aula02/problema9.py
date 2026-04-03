impostos = {"MG": 7, "SP": 12, "RJ": 15, "MS": 8}
val_prod = float(input("Digite o valor do produto: "))
estado = input("Digite o estado: ")

if estado not in impostos.keys():
    print("Estado Inválido")
else:
    valor = val_prod * (1+(impostos[estado]/100))
    print(f"Valor final: {valor:.2f}")
    
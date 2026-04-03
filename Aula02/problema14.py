a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

delta = b**2 - 4*a*c

if delta < 0:
    print("Não existe raiz real")
elif delta == 0:
    raiz = -b / (2*a)
    print(f"Raiz única")
    print(f"Raiz: {raiz:.2f}")
else:
    raiz1 = (-b + delta**0.5) / (2*a)
    raiz2 = (-b - delta**0.5) / (2*a)
    print(f"Raiz 1: {raiz1:.2f}")
    print(f"Raiz 2: {raiz2:.2f}")

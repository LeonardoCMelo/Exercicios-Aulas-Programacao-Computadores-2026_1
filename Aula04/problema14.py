massa = float(input("Insira a massa inicial: "))
tempo = 0

while massa>=0.25:
    massa = massa/2
    tempo += 50

print(f"Tempo necessário (em s): {tempo}")
print(f"Massa restante (em g): {massa:.2f}")

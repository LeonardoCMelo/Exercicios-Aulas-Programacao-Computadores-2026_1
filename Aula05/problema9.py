palavra = input("Entrada: ")

peso = 0

for p in palavra:
    if p == 'a':
        peso += 1
    elif p == 'e':
        peso += 3
    elif p == 'i':
        peso += 5
    elif p == 'o':
        peso += 7
    elif p == 'u':
        peso += 9

print(f"Soma: {peso}")

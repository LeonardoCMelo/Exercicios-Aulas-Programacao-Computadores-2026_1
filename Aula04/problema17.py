n = int(input("Digite um número: "))

maior = 0
menor = n if n>=0 else 0

while n >= 0:
    n = int(input("Digite um número: "))
    if n > maior:
        maior = n
    if n < menor and n>=0:
        menor = n

print (f"Maior: {maior}")
print (f"Menor: {menor}")
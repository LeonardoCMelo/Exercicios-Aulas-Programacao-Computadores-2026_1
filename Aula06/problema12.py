div = int(input("Digite o divisor: "))
lista = []

num = 0

while num>=0:
    num = int(input("Digite um inteiro: "))
    if num % div == 0 and num>0:
        lista.append(num)
print(f"Resultado: {lista}")

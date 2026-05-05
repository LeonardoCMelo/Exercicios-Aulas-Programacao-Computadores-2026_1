n, quant_par, quant_impar = 0, 0, 0

while n >= 0:
    n = int(input("Digite um número: "))
    if n>0:
        if n%2==0:
            quant_par += n
        else:
            quant_impar += n

print(f"Soma pares: {quant_par}")
print(f"Soma ímpares: {quant_impar}")

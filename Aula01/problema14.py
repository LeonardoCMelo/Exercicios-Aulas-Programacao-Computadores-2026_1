num = int(input("Digite um inteiro de 4 algarismos: "))

u = num % 10
d = (num % 100 - u)/10
c = (num % 1000 - num % 100) / 100
m = (num - num%1000)/1000

soma = int(m+c+d+u)

print(f"Resultado: {soma}")
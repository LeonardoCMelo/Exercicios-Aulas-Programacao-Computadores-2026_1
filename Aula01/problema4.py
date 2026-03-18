valor = int(input("Digite um inteiro de 4 algarismos: "))

u = valor % 10
d = (valor % 100 - u)/10
c = (valor % 1000 - valor % 100) / 100
m = (valor - valor%1000)/1000
inv = u*1000 + d*100 + c*10 + m

print(f"Valor invertido: {int(inv)}")

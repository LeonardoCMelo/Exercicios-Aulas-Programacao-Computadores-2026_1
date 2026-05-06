num = 0
raiz = []

while num >=0:
    num = int(input("Digite um inteiro: "))
    if num>0 and (num**(1/2))%1==0:
        raiz.append(num)

raiz.sort()
print(f"Resultado: {raiz}")
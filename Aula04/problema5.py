n = int(input("Digite um inteiro n: "))

isPrime = True

for i in range(n-1,1,-1):
    if n%i==0 and isPrime:
        isPrime = False
print("É primo" if isPrime else "Não é primo")

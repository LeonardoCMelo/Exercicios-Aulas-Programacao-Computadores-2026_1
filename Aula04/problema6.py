n = int(input(("Digite um inteiro n: ")))

if n == 1 or n == 2:
    print("1")
else:
    a, b = 1, 1
    for i in range(3, n+1):
        a, b = b, a+b
    print(b)

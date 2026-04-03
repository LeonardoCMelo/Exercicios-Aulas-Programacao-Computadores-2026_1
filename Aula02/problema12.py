x = int(input("Digite o comprimento do primeiro lado: "))
y = int(input("Digite o comprimento do segundo lado: "))
z = int(input("Digite o comprimento do terceiro lado: "))

if z > (x + y) or y > (x + z) or x > (y + z):
    print("Não é um triângulo")
else:
    if x == y and x == z:
        print("Triângulo Equilátero")
    elif x == y or x == z or y == z:
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")

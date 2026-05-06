ip = input("").split('.')

isValid = True

for i in ip:
    if (int(i)>255 or int(i)<0) and isValid:
        isValid = False

print("Válido" if isValid else "Inválido")

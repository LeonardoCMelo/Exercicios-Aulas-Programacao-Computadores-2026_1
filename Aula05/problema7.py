palavra = input("Digite uma palavra: ")
chave = int(input("Digite o valor da chave: "))
resultado = ""

for i in range(len(palavra)):
    temp = ord(palavra[i])
    temp += chave
    if temp > ord('z'):
        temp -= (ord('z')-ord('a')+1)
    resultado += chr(temp)

print(f"Resultado: {resultado}")

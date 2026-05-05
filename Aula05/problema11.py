frase = input("")

for i in range(len(frase)):
    if frase[i] in "AEIOUaeiou":
        print(f"{i} {frase[i]}")

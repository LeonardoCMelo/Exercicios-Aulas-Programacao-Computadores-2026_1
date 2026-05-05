frase = input("Frase embaralhada: ")

new_frase = frase[(len(frase)//2)-1::-1] + frase[len(frase):len(frase)//2-1:-1]

print(f"Frase correta: {new_frase}")

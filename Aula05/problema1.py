name = input("")
inicio_sobrenome = name.rfind(' ')
print(f"Nome formatado: {name[inicio_sobrenome+1:]}, {name[:inicio_sobrenome]}")

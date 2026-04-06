def peso_ideal(altura, sexo):
    if sexo == 'M':
        peso = (72.7 * altura) - 58
    elif sexo == 'F':
        peso = (62.1 * altura) - 44.7
    return peso

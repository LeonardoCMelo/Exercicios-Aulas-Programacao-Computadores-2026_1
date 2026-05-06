def tamanho_maior_string(elements):
    maior = 0
    for e in elements:
        if len(e)>maior:
            maior = len(e)
    return maior

def nested_sum(lista):
    soma = 0
    for i in lista:
        soma += sum(i)
    return soma

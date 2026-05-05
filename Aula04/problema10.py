def soma_divisores(entrada):
    soma = 0
    for i in range(1,entrada):
        if entrada%i == 0:
            soma += i
    return soma

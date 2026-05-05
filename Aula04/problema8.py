def quantidade_pares(inicio, fim):
    num_par = 0
    for i in range(inicio, fim+1):
        if i%2==0:
            num_par += 1
    return num_par

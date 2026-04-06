def consumo(km, litros):
    consumo = km / litros
    if consumo < 8:
        return "Venda o carro!"
    elif consumo <= 12:
        return "Econômico!"
    else:
        return "Super econômico!"

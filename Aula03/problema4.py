def calcula_valor(preco_litros, litros, tipo):
    if tipo == 'a':
        if litros <= 20:
            desconto = 0.03
        else:
            desconto = 0.05
    elif tipo == 'g':
        if litros <= 20:
            desconto = 0.04
        else:
            desconto = 0.06
    valor_total = preco_litros * litros
    valor_desconto = valor_total * desconto
    valor_final = valor_total - valor_desconto
    return valor_final

def valor_energia(qtde_kwh, tipo):
    if tipo == 'R':
        if qtde_kwh <= 500:
            valor = qtde_kwh * 0.40
        else:
            valor = qtde_kwh * 0.65
    elif tipo == 'C':
        if qtde_kwh <= 1000:
            valor = qtde_kwh * 0.55
        else:
            valor = qtde_kwh * 0.60
    elif tipo == 'I':
        if qtde_kwh <= 5000:
            valor = qtde_kwh * 0.55
        else:
            valor = qtde_kwh * 0.60

    return valor

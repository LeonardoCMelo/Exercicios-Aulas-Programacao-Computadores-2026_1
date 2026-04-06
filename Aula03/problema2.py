def pagamento(valor_hora, quant_horas):
    salario = valor_hora * quant_horas
    if salario <= 900:
        return salario
    elif salario <= 1500:
        return salario * 0.95
    elif salario <= 2500:
        return salario * 0.9
    else:
        return salario * 0.8

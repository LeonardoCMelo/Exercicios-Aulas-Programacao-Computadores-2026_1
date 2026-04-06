def pagamento(salario_atual):
    if salario_atual <= 280:
        return salario_atual * 1.2
    elif salario_atual <=700:
        return salario_atual * 1.15
    elif salario_atual <= 1500:
        return salario_atual * 1.1
    else:
        return salario_atual * 1.05

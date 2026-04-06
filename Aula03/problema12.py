def estacionamento(hc, mc, hp, mp):
    inicio = hc * 60 + mc
    fim = hp * 60 + mp

    if fim <= inicio:
        minutos = (24 * 60) + fim - inicio
    else:
        minutos = fim - inicio

    tempo = minutos // 60
    if minutos % 60 > 0:
        tempo += 1

    if tempo <= 2:
        valor = tempo * 1.0
    elif tempo <= 4:
        valor = tempo * 1.4
    else:
        valor = tempo * 2.0

    return valor
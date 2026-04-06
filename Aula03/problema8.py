def estacionamento(hc, mc, hp, mp):
    valor_hora = 1
    tempo_chegada = hc * 60 + mc
    tempo_partida = hp * 60 + mp
    duracao = tempo_partida - tempo_chegada
    horas = duracao // 60
    minutos = duracao % 60
    if minutos > 0:
        horas += 1
    valor_total = horas * valor_hora

    return valor_total

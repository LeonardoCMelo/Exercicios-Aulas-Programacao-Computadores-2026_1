
indice = []

indice.append(float(input("Qual o Índice Pluviométrico do dia 1? ")))

i_min = indice[0]
d_min = 1

for i in range(1,7):
    indice.append(float(input(f"Qual o Índice Pluviométrico do dia {i+1}? ")))
    if indice[i]<i_min:
        i_min = indice[i]
        d_min = i+1

media = sum(indice)/len(indice)

print(f"Índice Médio: {media:.2f}")
print(f"Índice Mínimo: {i_min:.2f}")
print(f"Dia do Mínimo: {d_min}")

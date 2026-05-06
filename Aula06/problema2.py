salto = []
for i in range(5):
    salto.append(float(input("")))

salto.remove(max(salto))
salto.remove(min(salto))

media = sum(salto)/len(salto)

print(f"Média: {media:.2f}")
temperatura = []

for i in range(12):
    temperatura.append(int(input()))

media = sum(temperatura)/len(temperatura)

print(f"Média: {media:.2f}")
for t in temperatura:
    if t > media:
        print(t)

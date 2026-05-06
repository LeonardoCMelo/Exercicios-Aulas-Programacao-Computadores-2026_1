vec1 = []
vec2 = []

dim = int(input("Digite a dimensão: "))

for _ in range(dim):
    vec1.append(int(input()))

for _ in range(dim):
    vec2.append(int(input()))

prod = 0

for i in range(dim):
    prod += vec1[i]*vec2[i]

print(f"Produto Escalar: {prod}")

p1 = input("Digite a primeira palavra: ")
p2 = input("Digite a segunda palavra: ")

combo = ""
min_length = min(len(p1), len(p2))

for i in range(min_length):
    combo += p1[i] + p2[i]

combo += p1[min_length:] if len(p1) > len(p2) else p2[min_length:]

print(f"Combinação: {combo}")

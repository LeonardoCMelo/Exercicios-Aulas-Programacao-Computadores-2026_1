l1 = []
l2 = []
inter = []

for i in range(5):
    l1.append(int(input()))

for i in range(5):
    l2.append(int(input()))

for n in l1:
    if l2.count(n)>0:
        inter.append(n)

print(f"Interseção: {inter}")
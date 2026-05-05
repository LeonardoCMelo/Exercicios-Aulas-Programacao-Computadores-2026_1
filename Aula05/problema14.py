f1 = input("").split()
f2 = input("").split()

min_length = min(len(f1), len(f2))

for i in range(min_length):
    if i%2!=0:
        f1[i], f2[i] = f2[i], f1[i]

print(" ".join(f1))
print(' '.join(f2))

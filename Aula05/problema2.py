palavra = input()
i=0
while i < len(palavra)-1:
    if palavra[i] == palavra[i+1]:
        palavra = palavra[:i]+palavra[i].upper() + palavra[i+2:]
    i+=1
print(palavra)

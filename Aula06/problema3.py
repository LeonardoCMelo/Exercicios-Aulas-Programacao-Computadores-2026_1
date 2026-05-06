num = []
par = []
impar = []
for i in range(5):
    num.append(int(input()))
    temp = num[len(num)-1]
    if temp%2==0:
        par.append(temp)
    else:
        impar.append(temp)
print(num)
print(par)
print(impar)

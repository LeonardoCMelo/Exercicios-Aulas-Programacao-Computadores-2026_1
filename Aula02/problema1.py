nums = []

max = 0
div3 = 0
nums.append(int(input("Digite o primeiro inteiro: ")))

min = nums[0]

nums.append(int(input("Digite o segundo inteiro: ")))
nums.append(int(input("Digite o terceiro inteiro: ")))
nums.append(int(input("Digite o quarto inteiro: ")))
nums.append(int(input("Digite o quinto inteiro: ")))

for num in nums:
    if num>max:
        max = num
    if num<min:
        min = num
    if num%3==0:
        div3 += 1

print(f"Maior: {max}")
print(f"Menor: {min}")
print(f"Quantidade de divisíveis por 3: {div3}")

nums = []

for _ in range(10):
    nums.append(int(input()))

avg = sum(nums)/len(nums)

desvio = ((1 / (len(nums) - 1))*(sum((n-avg)**2 for n in nums)))**(1/2)

print(f"Desvio Padrão: {desvio:.2f}")
num = input("")

mult = None
trio = ""

for i in range(len(num)-3):
    mult_temp = int(num[i])*int(num[i+1])*int(num[i+2])
    if mult==None or mult_temp>mult:
        mult = mult_temp
        trio = num[i:i+3]

print(trio)

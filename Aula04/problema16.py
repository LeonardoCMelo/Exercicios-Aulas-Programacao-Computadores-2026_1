v_0 = float(input("Digite a velocidade inicial: "))
s_0 = float(input("Digite a posição inicial: "))
acc = float(input("Digite a aceleração: "))
tempo = int(input("Digite os segundos a serem avaliados: "))

for t in range(tempo):
    S = s_0 + v_0*t + (acc*t**2)/2
    V = v_0 + acc*t
    print(f"t = {t} s; V = {V:.1f} m/s; S = {S:.1f} m")

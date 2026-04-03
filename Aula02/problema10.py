dia_mes = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9:30, 10: 31, 11: 30, 12: 31}

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

if bissexto:
    dia_mes[2] = 29

if mes not in dia_mes.keys() or dia>dia_mes[mes]:
    print("Data inválida")
else: 
    print("Data válida")

time = int(input("Digite o valor do tempo em segundos: "))
hours = time // 3600
minutes = (time % 3600) // 60
seconds = time % 60
print(f"Valor convertido: {int(hours)} h {int(minutes)} min {int(seconds)} s")

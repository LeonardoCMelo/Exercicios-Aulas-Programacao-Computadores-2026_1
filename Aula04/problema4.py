preco_pao = float(input("Digite o preço do pão: "))
for i in range(50):
    print(f"{i+1} - R$ {((i+1)*preco_pao):.2f}")

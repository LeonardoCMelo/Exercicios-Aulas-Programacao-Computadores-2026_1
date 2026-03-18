valorVenda = float(input("Digite o valor da compra: "))

print(f"Valor com desconto: {(valorVenda*0.9):.2f}")
print(f"Valor da parcela: {(valorVenda/10):.2f}")
print(f"Comissão do vendedor (à vista): {(valorVenda*0.045):.2f}")
print(f"Comissão do vendedor (parcelado): {(valorVenda*0.05):.2f}")
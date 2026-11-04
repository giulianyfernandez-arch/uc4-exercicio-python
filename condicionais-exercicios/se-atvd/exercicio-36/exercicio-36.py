quantidade = int(input("Digite a quantidade de maçãs compradas: "))

if quantidade < 12:
    preco_unitario = 0.30
else:
    preco_unitario = 0.25

valor_total = quantidade * preco_unitario

print(f"Valor total da compra: R$ {valor_total:.2f}")
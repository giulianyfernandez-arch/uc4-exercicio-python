total = 0.0
while True:
    preco = float(input("Digite o preço do produto: "))
    total += preco
    resposta = input("Deseja adicionar outro produto? (sim/não): ")

    if resposta.lower() == "não":
        break

print(f"O total da compra é: R${total:.2f}")
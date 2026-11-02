qtd_livros = int(input("informe o número de livros: "))
qtd_jogos = int(input("informe o número de jogos: "))
valor_total = float(input("informe o valor total da compra: "))

if qtd_livros >= 2 or qtd_jogos >= 3:
    valor_total -= 25   

print(f"o valor total da compra: {valor_total}")
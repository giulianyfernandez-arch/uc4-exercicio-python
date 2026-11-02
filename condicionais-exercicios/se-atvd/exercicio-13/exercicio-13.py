qtd_jogos = int(input("Informe a quantidade de jogos: "))
valor_compra = float(input("informe o valor da compra: "))
pontuacao_inicial = int(input("informe a pontuacao inicial: "))

pontuacao_final = pontuacao_inicial

if qtd_jogos >= 3 and valor_compra > 500:
    pontuacao_final = pontuacao_inicial + 200

print(f"A pontuação final é: {pontuacao_final}")

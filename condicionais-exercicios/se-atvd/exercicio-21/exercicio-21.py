qtd_curtidas = int(input("informe o número de curtidas: "))
qtd_comentarios = int(input("informe o número de comentários: "))
pontos_iniciais = int(input("informe os pontos iniciais: "))

if qtd_curtidas > 100 and qtd_comentarios > 30:
    pontos_iniciais += 50

print(f"o total de pontos: {pontos_iniciais}")
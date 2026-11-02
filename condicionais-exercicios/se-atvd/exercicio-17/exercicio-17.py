reproducoes = int(input("informe o número de reproduções: "))
qtd_curtidas = int(input("informe o número de curtidas: "))
valor_arrecadado = float(input("informe o valor arrecadado: "))

if reproducoes > 1000 or qtd_curtidas > 200:
    valor_arrecadado += 150

print(f"o valor arrecadado: {valor_arrecadado}")

laboratorios_visitados = int(input("informe o número de laboratórios visitados: "))
pontos = laboratorios_visitados * 10

if laboratorios_visitados >= 4:
    pontos += 20

print(f"o total de pontos: {pontos}")
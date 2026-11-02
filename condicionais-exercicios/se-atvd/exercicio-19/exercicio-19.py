inscritos = int(input("informe o número de inscritos: "))
cadeiras_disponiveis = int(input("informe o número de cadeiras disponíveis: "))

if inscritos > 80 and cadeiras_disponiveis < 80:
    cadeiras_disponiveis += 30

print(f"o número de cadeiras disponíveis: {cadeiras_disponiveis}")
qtd_execucoes = int(input("informe o número de execuções: "))
numero_inicial_musica = int(input("informe o número inicial da música: "))

if qtd_execucoes >= 10:
    numero_inicial_musica += 5
    print(f"meta alcançada! +5 músicas: {numero_inicial_musica}")

else:
    print(f"meta não alcançada! número inicial da música: {numero_inicial_musica}")
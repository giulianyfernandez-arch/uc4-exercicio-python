temperaturas = [28, 30, 27, 31, 29]

print("Temperaturas registradas:", temperaturas)

indice = 0
while indice < len(temperaturas):
    print(f"Dia {indice + 1}: {temperaturas[indice]}°C")
    indice += 1

print("Quantidade de registros:", len(temperaturas))
print("Maior temperatura:", max(temperaturas))
print("Menor temperatura:", min(temperaturas))
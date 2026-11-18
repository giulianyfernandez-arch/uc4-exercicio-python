contador = 1
positivos = 0

while contador <= 8:
    numero = int(input("digite o numero inteiro: "))
    if numero > 0:
        positivos += 1
    contador += 1

print(f"Quantidade de números positivos: {positivos}")
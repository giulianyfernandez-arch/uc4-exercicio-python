distancia = float(input("informe a distância percorrida em km: "))
valor = 180 

if distancia > 10:
    valor += 25

print(f"o valor cobrado será: {valor}")

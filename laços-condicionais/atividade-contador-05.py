cofrinho = 0
contador = 1

while contador <= 5:
    valor = float(input(f"Digite o valor do {contador}º depósito: "))
    cofrinho += valor         
    contador += 1

print(f"O total de depósitos no cofrinho é: R${cofrinho:.2f}")
# Faça um algoritmo para ler o valor total de uma compra e o valor pago pelo cliente. O algoritmo deve calcular o troco subtraindo o valor pago do valor total da compra utilizando o operador de atribuição de subtração (-=). No final, o algoritmo deve imprimir o resultado do troco a ser entregue.

valor_total = float(input("digite o valor total: "))
valor_pago = float(input("digite o valor pago: "))

troco = valor_pago
troco -= valor_total

print(f"o troco a ser entregue:  {troco: .2f}")

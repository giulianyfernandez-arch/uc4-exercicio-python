saldo_creditos = int(input("informe o saldo de crédito: "))

if saldo_creditos < 20:
  saldo_creditos += 15

  print(f"o saldo atual é:  {saldo_creditos}")
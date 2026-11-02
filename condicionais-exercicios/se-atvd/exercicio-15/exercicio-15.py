custo_ingresso = 750
custo_passagem = 300
valor_total = custo_ingresso + custo_passagem

dinheiro_mika = float(input("quanto mika possui? "))

if dinheiro_mika >= valor_total:
    dinheiro_mika += 100.00
    print("\nParabéns! A família deu R$ 100 extras para as lembrancinhas!")
else:
    print("\nAinda falta dinheiro para cobrir o ingresso e a passagem.")

print(f"Dinheiro total disponível ao final: R$ {dinheiro_mika}")
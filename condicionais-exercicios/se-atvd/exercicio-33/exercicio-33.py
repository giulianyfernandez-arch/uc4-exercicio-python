ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = 2026 

idade = ano_atual - ano_nascimento

if idade < 16:
    print(f"Idade aproximada: {idade} anos. Voto *proibido*.")
elif (16 <= idade < 18) or (idade >= 70):
    print(f"Idade aproximada: {idade} anos. Voto *opcional*.")
else:
    print(f"Idade aproximada: {idade} anos. Voto *obrigatório*.")
 # Faça um algoritmo para ler o ano de nascimento de uma pessoa e o ano atual. O algoritmo deve calcular a idade da pessoa e verificar se a idade é maior ou igual a 18 utilizando um operador relacional. No final, o algoritmo deve imprimir a idade e o resultado da verificação (um valor booleano: True ou False).

ano_nascimento = int(input("digite seu ano de nascimento: "))
ano_atual = int(input("digite o ano atual: "))

idade = ano_atual - ano_nascimento

maior_de_idade = idade >= 18

print(f"idade calculada:  {idade} anos")
print(f"maior de 18 anos? {maior_de_idade}")
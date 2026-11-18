idade = int(input("Digite a sua idade: "))

while idade < 18 or idade > 60:
    print("Idade inválida. A idade deve estar entre 18 e 60 anos.")
    idade = int(input("Digite a sua idade: "))

print("Idade válida. Você pode prosseguir com o cadastro.")
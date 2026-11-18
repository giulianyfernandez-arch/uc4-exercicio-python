tentativas = 0

while tentativas < 3:
    senha = input("Digite a senha: ")
    tentativas += 1

    if senha == "1234":
        print("Acesso concedido!")
        break  
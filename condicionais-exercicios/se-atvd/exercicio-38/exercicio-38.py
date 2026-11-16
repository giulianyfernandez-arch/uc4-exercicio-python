cargo = input("Digite o cargo (Administrativo / Operacional): ").strip().capitalize()
tempo_empresa = int(input("Digite o tempo de empresa (em anos): "))

if cargo == "Administrativo":
    if tempo_empresa >= 5:
        print("Funcionário Administrativo: Pode receber promoção! ")
    else:
        print("Funcionário Administrativo: Ainda não está apto.")

elif cargo == "Operacional":
    if tempo_empresa >= 3:
        print("Funcionário Operacional: Pode receber promoção! ")
    else:
        print("Funcionário Operacional: Ainda não está apto.")

else:
    print("Erro: Cargo inválido. Tente novamente.")
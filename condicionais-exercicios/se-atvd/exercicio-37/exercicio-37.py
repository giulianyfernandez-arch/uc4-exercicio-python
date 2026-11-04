pulseira = input("digite a cor da pulseira: ")

if pulseira == "vermelho":
    print("atendimento imediato")
elif pulseira == "amarelo":
    print("atendimento rapido")
elif pulseira == "verde":
    print("aguarde sua vez")
elif pulseira == "azul":
    print("encaminhado para o posto")
else:
    print("cor inválida")
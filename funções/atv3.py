def verificar_aprovacao(nota):
    if nota >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

resultado1 = verificar_aprovacao(8.5)
resultado2 = verificar_aprovacao(6.0)
resultado3 = verificar_aprovacao(7.0)

print(f"Estudante 1: {resultado1}")
print(f"Estudante 2: {resultado2}")
print(f"Estudante 3: {resultado3}")
notas = [8, 5, 9, 4, 7]
aprovados = 0
reprovados = 0

print("Notas registradas:", notas)

for nota in notas:
    if nota >= 7:
        print(f"Nota {nota}: Aprovado")
        aprovados += 1
    else:
        print(f"Nota {nota}: Reprovado")
        reprovados += 1

print(f"\nTotal de Aprovados: {aprovados}")
print(f"Total de Reprovados: {reprovados}")
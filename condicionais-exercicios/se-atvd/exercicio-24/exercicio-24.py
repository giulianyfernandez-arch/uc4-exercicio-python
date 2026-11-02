total_alunos = int(input("informe o total de alunos: "))
alunos_presentes = int(input("informe o número de alunos presentes: "))
media_turma = int(input("informe a média da turma: "))
preco_esfiha = 5

if alunos_presentes == total_alunos and media_turma >= 8:
    custo_total = alunos_presentes * preco_esfiha
    print(f"o custo total das esfihas será: {custo_total}")

else:
    print("não será possível comprar as esfihas")
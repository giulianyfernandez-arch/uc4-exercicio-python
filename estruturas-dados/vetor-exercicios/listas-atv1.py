livros = ["Dom Casmurro", "1984", "O Alquimista", "O Pequeno Príncipe"]

print("--- Livros Cadastrados Inicialmente ---")
print(livros)

livros.append("O Hobbit")

if "1984" in livros:
    livros.remove("1984")

livros.insert(1, "A Revolução dos Bichos")

livros.sort()

print("\n--- Lista Final de Livros (Ordem Alfabética) ---")
for livro in livros:
    print(f"- {livro}")

print(f"\nQuantidade total de livros cadastrados: {len(livros)}")
passageiros = ["Miguel", "Giuliany", "Rhaldney", "Mikaelly", "Kauany"]

print("Passageiros iniciais:", passageiros)

passageiros.append("Cauã")

if "Jonatha" in passageiros:
    passageiros.remove("Jonatha")

indice_mikaelly = passageiros.index("Mikaelly")
passageiros[indice_mikaelly] = "Anna"

print("Quantidade atual de passageiros:", len(passageiros))

print("\n--- Lista Final de Passageiros ---")
for p in passageiros:
    print(p)
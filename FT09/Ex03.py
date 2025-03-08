"""Efetua um programa em python:
a. Instancie o seguinte dicionário:
Computadores_1 = {
    "Marca": "Asus",
    "Ecra": "14Pol",
    "RAM": [4, 8, 12]
    1 de 2
}
b. Acrescente um novo elemento à lista com chave igual a “Disco” e
valor[“128G”, “256G”]
c. Permita ao utilizador introduzir um valor específico de RAM e
verificar se esta está presente na lista.
d. Acrecente 16 como novo valor de RAM.
e. Copie o dicionário para um novo usando Deep Copy().
f. Na lista nova modifique a marca para “Lenovo” e os valores da RAM
para[4, 8]. Imprima a nova lista
g. Crie uma nova lista com deep copy e modifique a marca para “HP” e
Disco para[“256G”] - Imprima a respetiva lista
h. Cria uma lista cujos elementos são os três dicionários.
i. Imprima as marcas com 128G de RAM
j. Imprima as marcas com 8 e 12 de RAM """

import copy

# a. Instanciar o dicionário
Computadores_1 = {
    "Marca": "Asus",
    "Ecra": "14Pol",
    "RAM": [4, 8, 12]
}

# b. Acrescentar um novo elemento à lista com chave igual a “Disco”
Computadores_1["Disco"] = ["128G", "256G"]

# c. Permitir ao utilizador introduzir um valor específico de RAM e verificar se está presente
valor_ram = int(input("Introduza um valor de RAM para verificar: "))
if valor_ram in Computadores_1["RAM"]:
    print(f"O valor {valor_ram} está presente na lista de RAM.")
else:
    print(f"O valor {valor_ram} não está presente na lista de RAM.")

# d. Acrescentar 16 como novo valor de RAM
Computadores_1["RAM"].append(16)

# e. Copiar o dicionário para um novo usando Deep Copy
Computadores_2 = copy.deepcopy(Computadores_1)

# f. Modificar a marca para “Lenovo” e os valores da RAM para [4, 8]
Computadores_2["Marca"] = "Lenovo"
Computadores_2["RAM"] = [4, 8]
print("Nova lista (Computadores_2):", Computadores_2)

# g. Criar uma nova lista com deep copy e modificar a marca para “HP” e Disco para [“256G”]
Computadores_3 = copy.deepcopy(Computadores_1)
Computadores_3["Marca"] = "HP"
Computadores_3["Disco"] = ["256G"]
print("Lista modificada (Computadores_3):", Computadores_3)

# h. Criar uma lista cujos elementos são os três dicionários
lista_computadores = [Computadores_1, Computadores_2, Computadores_3]

# i. Imprimir as marcas com 128G de RAM
print("Marcas com 128G de RAM:")
for computador in lista_computadores:
    if "128G" in computador.get("Disco", []):
        print(computador["Marca"])

# j. Imprimir as marcas com 8 e 12 de RAM
print("Marcas com 8 e 12 de RAM:")
for computador in lista_computadores:
    if 8 in computador["RAM"] or 12 in computador["RAM"]:
        print(computador["Marca"])

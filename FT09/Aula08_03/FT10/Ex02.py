# Reproduz o seguinte programa

prov = """o pior cego é aquele que nãs quer ver."""

# Primeira letra da frase em maiúsculas

prov = prov.capitalize()
print(prov)

# Separar as palavras da frase onde ocorre espaço e transformar a frase numa lista
palavra = prov.split(" ")
print(palavra)

# Contar a ocorrência duma palavra numa frase

count = 0

for x in palavra:
    if "que" in x:
        count = count+1

print(count)

# Substituir uma parte da frase por outra

prov = prov.replace("quer ver", "compra um cão")
print(prov)

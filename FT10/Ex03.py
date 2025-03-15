"""Considere a seguinte variável que armazena uma string com um conjunto de
datas separadas pelo caracter “, ”."""

# a. Armazene as diferentes datas numa string;
datas = "12ago2021,02set2020,20jan2022,11out2019,09mar2020,10dez2022"

# b. Imprimir as datas correspondentes ao ano de 2022
datas_lista = datas.split(",")  # Divide a string em uma lista de datas
# Filtra as datas de 2022
datas_2022 = [data for data in datas_lista if "2022" in data]

print("Datas correspondentes ao ano de 2022:")
for data in datas_2022:
    print(data)

# c. Criar uma nova lista (dias) e armazenar o dia de cada uma das datas
dias = [int(data[:2]) for data in datas_lista]  # Extrai o dia de cada data

# Ordenar a lista de forma crescente
dias.sort()

# Imprimir a lista ordenada
print("\nLista de dias ordenada:")
print(dias)

""" Considera a seguinte lista: 
nums=[10, 2.5, 7, 11, 7.9, "Python", True,6, 5.8 , "Listas"] 
Efetua um programa em python que: 
a. Imprima a quantidade de inteiros, floats, strings e boleanos na lista; 
b. Efetua a média de todos os valores inteiros na lista. 
c. Crie e retorne uma nova lista só com os valores inteiros"""

# Lista fornecida
nums = [10, 2.5, 7, 11, 7.9, "Python", True, 6, 5.8, "Listas"]

# a. Imprime a quantidade de inteiros, floats, strings e booleanos na lista
contagem = {
    'inteiros': 0,
    'floats': 0,
    'strings': 0,
    'booleanos': 0
}

# Lista para armazenar os inteiros
lista_inteiros = []

# Itera sobre a lista para contar os tipos e coletar inteiros
for item in nums:
    if isinstance(item, int):
        contagem['inteiros'] += 1
        lista_inteiros.append(item)  
    elif isinstance(item, float):
        contagem['floats'] += 1
    elif isinstance(item, str):
        contagem['strings'] += 1
    elif isinstance(item, bool):
        contagem['booleanos'] += 1

# Imprime a contagem
print("Quantidade de inteiros:", contagem['inteiros'])
print("Quantidade de floats:", contagem['floats'])
print("Quantidade de strings:", contagem['strings'])
print("Quantidade de booleanos:", contagem['booleanos'])

# b. Efetua a média de todos os valores inteiros na lista
if contagem['inteiros'] > 0:
    media_inteiros = sum(lista_inteiros) / contagem['inteiros']
    print("Média dos valores inteiros:", media_inteiros)
else:
    print("Não há valores inteiros para calcular a média.")

# c. Cria e retorna uma nova lista só com os valores inteiros
print("Nova lista com valores inteiros:", lista_inteiros)
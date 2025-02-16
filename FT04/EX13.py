"""Elabora um programa para soma todos os valores entre 10 e 100 (inclusive) e apresentar os valores
no ecrã."""

soma = 0

for i in range(10, 101):
    soma += i
    print(i) 

#
print(f"A soma de todos os números entre 10 e 100 é: {soma}")
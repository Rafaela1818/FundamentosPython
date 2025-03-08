"""Escreve um programa que, dada uma sequência de números inteiros
(todos fornecidos na mesma linha, separados por espaços), 
imprima a média desses número."""

numeros = [int(i) for i in input(
    "Introduza uma sequencia de 10 numeros separados por espaço").split()]
print(f"A média dos números introduzidos é {sum(numeros)/len(numeros)}")

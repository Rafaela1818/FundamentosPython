"""Considera a lista: 
notas=[11.2, 15, 8.7, 17.2, 7.9 ] 
Cria um programa, em python, que: 
a. Acrescenta o valor 10.9 no final da lista e faz o print de toda a lista 
b. Faz o print do tamanho da lista 
c. Faz o print do valor mínimo da lista 
d. Faz a média dos valores da lista"""

notas = [11.2, 15, 8.7, 17.2, 7.9] 

notas.append(10.9)
print(notas)

tamanho_lista = len(notas)
print(tamanho_lista)

nota_min=min(notas)
print(nota_min)

soma= sum(notas)
media = soma / tamanho_lista
print(media)


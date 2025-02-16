"""Escreve um programa que calcule e escreva o resultado do fatorial de um número inteiro positivo N
sabendo que: n!=1*2*3*…*n"""

n=int(input("Digite um número inteiro positivo N:"))

fatorial= 1

for i in range(1, n + 1):
    fatorial *= i 
    print (f"o fatorial de {n} é: {fatorial}")
"""Escreve um programa que calcule e escreva o resultado do fatorial de um número inteiro positivo N
sabendo que: n!=1*2*3*…*n"""

N = int(input("Digite um número inteiro positivo: "))
fatorial = calcular_fatorial(N)
print(f"Fatorial de {N}: {fatorial}")

def calcular_fatorial(n):
    if n < 1:
        return "N deve ser um número inteiro positivo (N >= 1)"
    
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    
    return fatorial
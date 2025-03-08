"""Escreve um programa que, dada uma sequência de números inteiros
(todos fornecidos na mesma linha, separados por espaços), 
imprima a média desses número."""

# Solicitar ao usuário que insira uma sequência de números inteiros
entrada = input(
    "Digite uma sequência de números inteiros, separados por espaços: ")

# Dividir a entrada em uma lista de strings e converter para inteiros
numeros = list(map(int, entrada.split()))

# Calcular a média
if len(numeros) > 0:  # Verifica se a lista não está vazia
    media = sum(numeros) / len(numeros)
    print(f"A média dos números é: {media}")
else:
    print("Nenhum número foi fornecido.")

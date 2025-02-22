"""Escreva um programa que peça ao utilizador números entre 0-10. Se o utilizador inserir um número
fora desse intervalo o programa deverá finalizar com uma mensagem personalizada."""""

n= int(input("Digite um número de 1 a 10: "))

if 0 <= n <= 10:
        print(f"Você digitou: {n}")
else:
    print("Este número não está dentro do intervalo solicitado.")

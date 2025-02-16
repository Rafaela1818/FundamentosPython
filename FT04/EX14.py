"""Elabora um programa que pede ao utilizador para inserir dois números inteiros. O programa deve
escrever todos os números inteiros entre os dois limites por ordem crescente. Utiliza o ciclo for."""

limite_inferior = int(input(Digite o primeiro número:))
limite_superior = int(input(Digite o segundo número:))

if limite_inferior < limite_superior:

    for i in range(limite_inferior + 1, limite_superior):
        print(i)
else:
    print("O limite inferior deve ser menor que o limite superior.")
    
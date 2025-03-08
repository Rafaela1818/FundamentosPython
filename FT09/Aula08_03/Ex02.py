"""Escreve um programa que, dada ma String representando um texto, imprima o número de palavras existentes.
Observação:você deve remover os sinais de pontuação(".", ",",":","!" e "?") antes de realizar a contagem das palavras."""

import string

# Solicitar ao usuário que insira um texto
texto = input("Digite um texto: ")

# Definir os sinais de pontuação a serem removidos
sinais_de_pontuacao = ".,:!? "

# Remover os sinais de pontuação
texto_sem_pontuacao = texto.translate(
    str.maketrans("", "", sinais_de_pontuacao))

# Dividir o texto em palavras
palavras = texto.split()

# Contar o número de palavras
numero_de_palavras = len(palavras)

# Imprimir o resultado
print(f"O número de palavras no texto é: {numero_de_palavras}")

"""Elabora um programa para calcula a soma dos N primeiros números naturais (1+2+3+...+N)
em que N é um número introduzido pelo utilizador (NOTA: este programa poderia ser feito
utilizando a fórmula da progressão aritmética, S = (1+N) * N/2, mas faz de conta que não
sabíamos a fórmula)."""

# Solicita ao usuário que insira um número natural
N = int(input("Digite um número natural (N): "))

# Inicializa a variável para armazenar a soma
soma = 0

# Loop para calcular a soma dos N primeiros números naturais
for i in range(1, N + 1):
    soma += i  # Adiciona o número atual à soma

# Exibe o resultado
print(f"A soma dos {N} primeiros números naturais é: {soma}")
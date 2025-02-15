#Escreve um programa que calcule a soma e o produto dos N primeiros números naturais


N = int(input("Digite um número natural: "))
soma, produto = calcular_soma_produto(N)
print(f"Soma dos {N} primeiros números naturais: {soma}")
print(f"Produto dos {N} primeiros números naturais: {produto}")


def calcular_soma_produto(n):
    if n < 1:
        return "N deve ser um número natural (N >= 1)"
    
    soma = sum(range(1, n + 1))
    produto = 1
    for i in range(1, n + 1):
        produto *= i
    
    return soma, produto


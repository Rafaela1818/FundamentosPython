#Escreve um programa que coloque no ecrã os 10 primeiros números de forma decrescente.

N = int(input("Digite um número natural N: "))
soma, produto = soma_produto_naturais(N)
print(f"Soma dos {N} primeiros números naturais: {soma}")
print(f"Produto dos {N} primeiros números naturais: {produto}")

def soma_produto_naturais(n):
    if n < 1:
        return "N deve ser um número natural (N >= 1)"
    
    soma = sum(range(1, n + 1))
    produto = 1
    
    for i in range(1, n + 1):
        produto *= i
    
    return soma, produto


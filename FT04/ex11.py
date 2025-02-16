#Escreve um programa que calcule a soma e o produto dos N primeiros números naturais


N = int(input("Digite um número natural: "))


soma = 0
produto = 1


for i in range(1, N + 1):
    soma += i
    produto *= i

print(f"Soma dos {N} primeiros números naturais: {soma}")
print(f"Produto dos {N} primeiros números naturais: {produto}")

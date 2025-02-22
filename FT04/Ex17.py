""" Escreva um programa que peça ao utilizador 20 números reais e no final mostre a soma e a média
dos números introduzidos."""

soma = 0
for i in range(20):
    n= float (input("Digite um número real:"))
    soma += n
    
media= soma / 20

print(f" A soma dos números é:{soma}")
print(f"A média dos números é: {media}")

    

    
             
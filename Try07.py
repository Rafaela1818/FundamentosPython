"""Elabora um programa para calcula a soma dos N primeiros números naturais (1+2+3+...+N)
em que N é um número introduzido pelo utilizador (NOTA: este programa poderia ser feito
utilizando a fórmula da progressão aritmética, S = (1+N) * N/2, mas faz de conta que não
sabíamos a fórmula)."""

n= input("Introduza um número natural:")
while True:
    try:
        n=int(n)
        break
    except:
        print("O número introduzido não é válido")
        n=input("Introduza um número natural:")
        
soma= 0 
for i in range(1,n,+1):
    soma = soma +i
print("soma=", soma)
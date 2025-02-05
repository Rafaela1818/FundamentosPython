#Escreve um programa para classificar um triângulo de acordo com o comprimento dos seus lados. 

print("Introduza o cumprimento dos lados do triângulo:")
l1=input("Lado 1:")
l2=input("Lado 2:")
l3=input("Lado 3:")

if l1 == l2 == l3:
    print("O triangulo é Equilátero")
elif l1 != l2 and l1 != l3 and l2 != l3:
    print("O triangulo é Escaleno")
else:
    print("O triangulo é Isósceles")
    

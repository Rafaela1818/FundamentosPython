#Escreva um programa que verifique se um determinado número introduzido pelo utilizador é nulo, positivo ou negativo.

numero1 =float(input("Introduza um número: "))

if numero1 == 0:
    print("O número é nulo.")
elif numero1 > 0:
    print("O número é positivo.")
else:
    print("O número é negativo.")
    
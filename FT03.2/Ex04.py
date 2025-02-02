#Escreve um programa que receba dois números reais e indique qual o maior dos dois números. Considera a possibilidade de o utilizador indicar dois números iguais
# Solicita ao usuário que insira dois números

numero1 = float(input("Introduza o primeiro número: "))
numero2 = float(input("Introduza o segundo número: "))

if numero1 > numero2:
    print(f"O número {numero1} é maior.")
elif numero1 == numero2:
    print("Os números são iguais.")
else:  
    print(f"O número {numero2} é maior.")
 
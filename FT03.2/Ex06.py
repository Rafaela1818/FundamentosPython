#Escreve um programa que receba três números reais e indique qual o maior dos três números

import math

numero1=float(input("Introduza o primeiro número:"))
numero2=float(input("Introduza o segundo número:"))
numero3=float(input("Introduza o terceiro número:"))

maior = max(numero1, numero2, numero3) 
print("O maior número é:" , maior)

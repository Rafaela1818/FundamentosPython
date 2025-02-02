#Escreve um programa que solicite um número inteiro ao utilizador e caso o mesmo seja maior que 20, devolva o resultado da sua divisão por 2. 

import math

numero=int(input("Digite um numero inteiro:"))
if numero>20:
    numero=numero/2
    print(f"o numero dividido por 2 é :{ numero: .2f}")
    
else:print("O nunero indicado é inferior a 20.")

#Reescreve o programa anterior de forma a apresentar a tabuada de qualquer número introduzido pelo utilizador.

numero = int(input("Introduza um número:"))

for i in range(1, 11):  
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
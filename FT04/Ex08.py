# Escreve um programa que coloque no ecrã a tabuada do número 5.

numero = 5

for i in range(1, 11):  # De 1 a 10
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
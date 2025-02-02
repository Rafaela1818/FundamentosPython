#Escreve um programa que solicite a temperatura em Fahrenheit (F), ao utilizador, e a converta para grau Celsius (C), devolvendo o resultado da conversão.

Temperaturaf=float(input("Insira a temperatura em Fahrenheit:"))
Temperaturac=(Temperaturaf - 32)*5/9

print(f"A temperatura em °C é {Temperaturac: .2f} °C")
#Elabora um programa para verificar se um ano é bissexto ou não. A condição para ser 
#um ano bissexto é: o ano deve ser divisível por 400; ou se for divisível por 4 e não for divisível por 100.

ano_bissexto=int(input("Intruduza o ano:"))

if ano_bissexto % 400 == 0 or (ano_bissexto %4 == 0 and ano_bissexto %100 != 0):
     print("O ano é bissexto")
else:
     print("O ano não é bissexto")
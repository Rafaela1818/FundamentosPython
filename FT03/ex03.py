#Escreve um programa que solicite um número inteiro ao utilizador e verifique se o 
#mesmo é par ou ímpar. A mensagem no ecrã deverá ter o seguinte formato. A mensagem no ecra deverá ter a seguinte forma:

num1 = int(input("Digite um número inteiro: "))

if num1 % 2 == 0:
    print(f" O número {num1} é par")
else:
    print(f" O número {num1} é ímper")
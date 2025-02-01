#Escreve um programa que receba dois números reais e indique qual o maior dos dois números. 
# Considera a possibilidade de o utilizador indicar dois números iguais. 

num1 = input('Num 1: ')
num2 = input('Num 2: ')

num1, num2 = int(num1), int(num2)

if num1 == num2:
    print(f'Os números são igual')
else:
    maior = max(num1, num2)
    print(f'O número {maior} é maior')
    

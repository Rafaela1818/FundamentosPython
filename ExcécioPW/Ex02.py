# Escreva um programa que solicite ao utilizador dois números inteiros a operação matemática a ser realizada (+,-,* e /). 

num1=int(input("Introduza o primeiro número:"))
num2=int(input("Introduza o segundo número:"))

operação =input("Introduz ir a operação matemática (+,-,* e /): ")

match operação:
    case "+":
        resultado= num1 + num2
    case"-":
        resultado= num1 - num2
    case"*":
        resultado= num1 * num2
    case"/":
        resultado= num1 // num2
        if num2== 0:
        resultado= "Não é possivel dividir por zero"
    case _:
        resultado = "Operação invalida"
        print("O resultado é {resultado}")
        
            
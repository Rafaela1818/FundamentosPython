# Implemente uma calculadora simples com as operações aritméticas básicas. O utilizador deverá especificar a operação desejada (+,-,*,/) e, em seguida, inserir dois valores. 
#Caso, o utilizador escolha divisão e insira como valor do denominar 0 mostra uma 
#mensagem personalizada. Para os restantes casos, mostra no ecrã o resultado da 
#operação desejada.


calculadora =input("escolha uma operação +,-,*,/:")
valor1= float(input("Intrduza o primeiro valor:"))
valor2= float(input("Introduza o segundo valor:"))

if calculadora == "+":
    resultado = valor1 + valor2
    print(f"O resultado de {valor1} + {valor2} é: {resultado}")
elif calculadora == "-":
    resultado = valor1 - valor2
    print(f"O resultado de {valor1} - {valor2} é: {resultado}")
elif calculadora == "*":
    resultado = valor1 * valor2
    print(f"O resultado de {valor1} * {valor2} é: {resultado}")
elif calculadora == "/":
    if  valor2 == 0:
        print("Não é possível dividir por zero.")
    else:
        resultado = valor1 / valor2
        print(f"O resultado de {valor1} / {valor2} é: {resultado}")
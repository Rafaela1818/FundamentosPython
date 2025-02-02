#Escreve um programa que solicite um número inteiro ao utilizador e verifique se o mesmo é par ou ímpar. A mensagem no ecrã deverá ter o seguinte formato

numero=int(input("Insira um número:\n->"))
if numero %2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é impar.")
    
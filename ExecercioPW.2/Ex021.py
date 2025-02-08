#Escreva um programa em que utilizes a intrução while e que devolve a tabuada escolhida
tab = int(input("Digite um número para saber sua tabuada: "))
i = 1
while i <= 10:
    print(f"{tab} x {i} = {tab * i}")
    i += 1
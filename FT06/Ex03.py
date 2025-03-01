"""Considera a lista 
idades=[25, 15, 19, 22, 37, 78, 46, 2, 67] 
Cria um programa, em python, que: 
a. Indique quantas pessoas são menores de idade 
b. Ordene a lista por ordem decrescente 
c. Pede ao utilizador uma idade e verifica se essa idade está na lista.  
#- Se estiver faz print("A idade está na lista") 
#- Caso contrário faz o print("não existe ninguém com essa idade na lista") """

idades=[25, 15, 19, 22, 37, 78, 46, 2, 67]

n_menores=sum(1 for idade in idades if idade < 18)
print(n_menores)

idades.sort(reverse=True)
print(idades)


idade=int(input("Digite a sua idade:"))

if idade in idades:
    print("A idade está na lista")
else:
    print("Não existe ninguém com essa idade na lista")


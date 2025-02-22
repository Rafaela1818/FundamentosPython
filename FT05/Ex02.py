""" Crie um programa para controlar listas, com as seguintes funções: 
• Adicionar elemento no início; 
• Adicionar elemento no fim; 
• Remover elemento; 
• Tamanho da lista; 
• Imprimir elementos da lista; 
• Esvaziar lista;"""

num = list()
for i in range(5):
	n = int(input("introduza número inteiro:\n-->"))
	num.append(n)
	
print("...............Lista Introduzida.....................")
print(num)

print("...............Análise e Manipulação da Lista.....................")

#Adicionar um elemento ao início
num.insert(0,123)
print(num)


#Adicionar um elemento ao fim
num.insert(len(num),123)
print(num)
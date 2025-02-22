""" Crie um programa para controlar listas, com as seguintes funções: 
• Adicionar elemento no início; 
• Adicionar elemento no fim; 
• Remover elemento; 
• Tamanho da lista; 
• Imprimir elementos da lista; 
• Esvaziar lista;"""

lista=list()
while True:
    print("Meni:")
    print("\t1 Adicionar elemento no início")
    print("\t2  Adicionar elemento no fim")
    print("\t3 Remover elemento")
    print("\t4 Tamanho da lista")
    print("\t5 Imprimir elementos da lista")
    print("\t6 Esvaziar Lista")
    print("\t7 Sair")
    op=input("Introduza a sua opção:")
    match op:
        case '1':
            lista.insert(0, input("Introduza um valor a adicionar á lista:"))
            print(lista)
        case'2':
            lista.append(input("Introduza um valor a adicionar á lista:"))
            print(lista)
        case'3':
            print(lista)
            lista.remove(input("Qual o elemento a remover?"))
        case '4':
            print(f"A lista tem {len(lista):0>3d} elementos")
        case '5':
            print(lista)
        case'6':
            lista.clear()
            print("A lista foi limpa")
        case'7':
            break
        case _:
            print("Opção inválida")    
            
        
#Escreve um prigrama que receba o nome de um produto e o seu preço, e retorne o preço total considerado os descontos seguintes:

produto=(input("Introduza o produto:"))
preço=float(input("Introduza o preço:"))

match produto:
    case "smartphone":
        print("desconto de 10%")
    case "tablet":
       print("desconto de 15%")    
    case "laptop":
        print("desconto de 20%")    
    case _: 
        print("não haverá desconto")
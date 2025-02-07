#O Índice de Massa Corporal (IMC) é utilizado para medir o peso ideal de uma pessoa. 
#Escreve um programa que peça o nome, a idade, o peso e a altura do utilizado e que, de seguida, calcule e mostre o resultado do seu IMC e classifique esse resultado de 
#acordo com as seguintes condições:

print("Introduza os seguintes dados:")
nome=input("Nome:")
idade= int(input("Idade:"))
peso= float(input("Peso:"))
altura= float(input("Altura:"))

def classificar_imc(imc):
    if imc < 17:
        return "Muito abaixo do peso ideal"
    elif 17 <= imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Acima do peso"
    elif 30 <= imc < 35:
        return "Obesidade I"
    elif 35 <= imc < 40:
        return "Obesidade II (severa)"
    else :
        return "Obesidade III (mórbida)"

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2) 
    return imc
imc = calcular_imc(peso, altura)

print(f"Seu IMC é: {imc:.2f}, {classificar_imc(imc)}")


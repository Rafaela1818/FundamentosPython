#Elabora um programa para verificar se um ano é bissexto ou não. A condição para ser 
#um ano bissexto é: o ano deve ser divisível por 400; ou se for divisível por 4 e não for divisível por 100.

def is_bissexto(ano):
    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        return True
    else:
        return False

# Solicita ao usuário para inserir um ano
ano = int(input("Digite um ano: "))

# Verifica se o ano é bissexto e exibe o resultado
if is_bissexto(ano):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")

"""Considere a seguinte variável que armazena uma string com um conjunto de
datas separadas pelo caracter “, ”."""

# Definindo a variável Txt
Txt = """Python é uma linguagem de programação 
2 de 3 
de alto nível, interpretada de script, imperativa, orientada a objetos, 
funcional, de tipagem dinâmica e forte."""

# a. Imprimir o texto todo em maiúsculas
print("Texto em maiúsculas:")
print(Txt.upper())

# b. Pedir uma palavra ao utilizador e verificar se está no texto
palavra = input("\nDigite uma palavra para verificar se está no texto: ")
if palavra in Txt:
    print(f"A palavra '{palavra}' está no texto.")
else:
    print(f"A palavra '{palavra}' não está no texto.")

# c. Imprimir o número de vezes que a letra ‘O’ ocorre no texto
# Contamos 'O' em maiúsculas para não diferenciar
numero_de_O = Txt.upper().count('O')
print(f"\nA letra 'O' ocorre {numero_de_O} vezes no texto.")

# d. Substituir todas as ocorrências da letra ‘P’ no texto por ‘_’
Texto_substituido = Txt.replace('P', '_').replace(
    'p', '_')  # Substitui 'P' e 'p'
print("\nTexto com 'P' substituído por '_':")
print(Texto_substituido)

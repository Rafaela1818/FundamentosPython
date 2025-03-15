# Reproduz o seguinte programa.

txt = "uFcd || proGRAMação eM pyTHON"

# Imprimir texto

print(txt)

# Imprimir Texto sem espaçamento inicial

txt = txt.strip()
print(txt)
# Imprimir frase até á palavra na 13º posição

print(txt[:13])

# Imprimir últimos 5 caratcteres da frase
print(txt[-5])

# Imprimir frase em maiúsculas

txt = txt.upper()
print(txt)

# Formação de strings

nome = "Sandra Oliveira"

print("O {} gosta muito da {}" .format(nome, txt))

# alinea g)

print(f"O {nome} gosta muito da {txt}")

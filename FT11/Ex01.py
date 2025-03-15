"""Escreve uma função em Python que, dados a medida do comprimento dos três
 lados de um triângulo diga se o mesmo é equilátero, isósceles ou escaleno."""


def tipo_triangulo(lado1, lado2, lado3):
    # Verifica se os lados formam um triângulo
    if lado1 <= 0 or lado2 <= 0 or lado3 <= 0 or lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
        return "Os lados não formam um triângulo."

    # Determina o tipo de triângulo
    if lado1 == lado2 == lado3:
        return "Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return "Isósceles"
    else:
        return "Escaleno"


# Exemplo de uso da função
lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))

resultado = tipo_triangulo(lado1, lado2, lado3)
print(f"O triângulo é: {resultado}")

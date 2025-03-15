"""Escreve uma função em Python que, dados a medida do comprimento do lado de
 um quadrado imprima os valores do seu perímero e da sua área (area=lado x 
lado; perimetro = 4 x lado)."""


def calcula_quadrado(lado):
    """Calcula e imprime a área e o perímetro de um quadrado."""
    if lado <= 0:
        print("O comprimento do lado deve ser maior que zero.")
        return

    area = lado * lado  # Área do quadrado
    perimetro = 4 * lado  # Perímetro do quadrado

    print(f"A área do quadrado é: {area}")
    print(f"O perímetro do quadrado é: {perimetro}")

# Função principal para interagir com o usuário


def main():
    lado = float(input("Digite o comprimento do lado do quadrado: "))
    calcula_quadrado(lado)


# Chama a função principal
if __name__ == "__main__":
    main()

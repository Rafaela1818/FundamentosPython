import math

def volume_esfera(raio):
    return (4/3) * math.pi * (raio ** 3)

# Exemplo
if __name__ == "__main__":
    try:
        raio = float(input("Digite o valor do raio da esfera: "))
        print("O volume da esfera é:", volume_esfera(raio))
    except ValueError:
        print("Por favor, insira um número válido.")

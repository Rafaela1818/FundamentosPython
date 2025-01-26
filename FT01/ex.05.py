import math

def calcular_hipotenusa(a, b):
    return math.sqrt(a**2 + b**2)

# Exemplo de uso
if __name__ == "__main__":
    a = float(input("Digite o valor do cateto a: "))
    b = float(input("Digite o valor do cateto b: "))
    print("O valor da hipotenusa é:", calcular_hipotenusa(a, b))

#Fazer um programa para ler quatro números inteiros e positivos, calcular e devolver a sua média.

# Inicializa uma lista para armazenar os números
numeros = []

# Lê quatro números inteiros e positivos
for i in range(4):
    while True:
        try:
            numero = int(input(f"Digite o {i + 1}º número inteiro e positivo: "))
            if numero >= 0:  # Verifica se o número é positivo
                numeros.append(numero)
                break  # Sai do loop se o número for válido
            else:
                print("Por favor, digite um número positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

# Calcula a média
media = sum(numeros) / len(numeros)

# Exibe a média
print(f"A média dos números é: {media:.2f}")

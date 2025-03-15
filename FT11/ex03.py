"""3. Escreve uma função em Python que dada uma lista de números imprime a soma
 dos valores dessa lista, o número de elementos da lista e a media desses 
valores."""


def analisa_lista(numeros):
    """Imprime a soma, o número de elementos e a média de uma lista de números."""
    if not numeros:  # Verifica se a lista está vazia
        print("A lista está vazia.")
        return

    soma = sum(numeros)  # Calcula a soma dos valores
    numero_de_elementos = len(numeros)  # Conta o número de elementos
    media = soma / numero_de_elementos  # Calcula a média

    print(f"Soma dos valores: {soma}")
    print(f"Número de elementos: {numero_de_elementos}")
    print(f"Média dos valores: {media}")

# Função principal para interagir com o usuário


def main():
    # Exemplo de lista de números
    lista_numeros = [10, 20, 30, 40, 50]
    analisa_lista(lista_numeros)


# Chama a função principal
if __name__ == "__main__":
    main()

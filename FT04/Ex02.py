"""Implemente um programa que, dada uma letra (S, C ou V), indique o estado civil de
uma pessoa. """

# Solicita ao usuário que digite uma letra
letra = input("Digite a letra S, C, ou V: ").strip().upper()  # Remove espaços e converte para maiúsculas

# Usa a estrutura match para verificar o estado civil
match letra:
    case "S":
        print("Solteiro")
    case "C":
        print("Casado")
    case "V":
        print("Viúvo")
    case _:
        print("Letra inválida. Por favor, digite S, C ou V.")
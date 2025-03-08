"""Efetua um programa em python onde:
a. Cries um dicionário e efetues o respetivo print.
b. Acrescentes dois novos elementos ao dicionário.
c. Removes um dos elementos da lista
d. Efetues uma operação, à escolha, sobre os dados no dicionário"""

dicionario = {
    "nome": "João",
    "idade": 25,
    "curso": "Informática"
}
print('Dicionário:', dicionario)

dicionario["morada"] = "     Rua das Flores      "
dicionario["telefone"] = 912345678
dicionario.pop("idade")

dicionario = {}
for chave, valor in dicionario.items():
    if isinstance(valor, str):
        dicionario[chave.upper()] = valor.strip()
    else:
        dicionario[chave.upper()] = valor

# EQUIVALENTE USANDO COMPREHENSION
dicionario = {chave.upper(): valor.strip() if isinstance(
    valor, str) else valor for chave, valor in dicionario.items()}

print('Dicionário:', dicionario)

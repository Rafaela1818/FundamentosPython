# Passo 1 e 2: solicitar distância e combustível
distancia = float(input("Digite a distância percorrida (km): "))
combustivel =float(input("Digite a quantidade de combustível gasto (litros): "))

# converter para float
distancia = float(distancia)
combustivel = float(combustivel)

# Passo 4: calcular consumo (km/l)
consumo = distancia / combustivel

# Passo 5: mostrar mensagem de acordo com o consumo
print("O consumo médio do carro é:", consumo, "km/l".format(consumo))

if consumo < 8:
    print("Consumo elevado (pouco económico).")
elif consumo < 12:
    print("Consumo razoável.")
else:
    print("Consumo bom (carro económico).")
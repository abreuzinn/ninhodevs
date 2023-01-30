
while True:
    try:
        numCorridas = int(input("Número de corridas: "))
        break
    except:
        TypeError(print("Insira um número. Tente novamente."))

totalCorridas = []
n = 1
contador = numCorridas
while True:
    while contador > 0:
        try:
            corridas = float(input(f"Insira o valor da {n}ª corrida: "))
            n+=1
            totalCorridas.append(corridas)
            contador-=1
        except:
            TypeError(print("Insira um valor válido."))
    break
    
gastoCombustivel = float(input("Insira o valor gasto com combustível: "))

print(" ")
print(f"MÉDIA POR CORRIDA               R$ {(sum(totalCorridas)/numCorridas):.2f}")
print(f"TOTAL RECEBIDO NO DIA           R$ {sum(totalCorridas):.2f}")
print(f"VALOR GASTO COM COMBUSTÍVEL     R$ {gastoCombustivel:.2f}")
print(" ")
print(f"LUCRO TOTAL                     R$ {(sum(totalCorridas)-gastoCombustivel):.2f}")                   
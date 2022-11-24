print("Encontre os números pares entre dois números.")

nummin = int(input("Insira o número mínimo: "))
nummax = int(input("Insira o número máximo: "))

for i in range(nummin, nummax+1):
    if (i%2!=0):
        print(i)
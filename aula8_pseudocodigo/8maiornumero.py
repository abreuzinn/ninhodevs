maior = 0
n = 0.1

while (n > 0):
    n = float(input("Insira um número maior que 0: "))
    if (n > maior):
        maior = n

print(f"O maior número é {maior:.0f}.")
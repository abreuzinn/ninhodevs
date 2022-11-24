notas = []
notasacima = []

while len(notas) < 5:
    notas5 = float(input("Insira as 5 notas: "))
    notas.append(notas5)

soma = sum(notas)
media = soma/5

print(f"A soma das notas é {soma}.")
print(f"A média das notas é {media}.")

for n in notas:
    if n > media:
        notasacima.append(n)
print(f"""As notas acima da média são:
{notasacima}""")

s = (input("Insira seu sexo (F ou M):"))
a = float(input("Insira sua altura:"))

if s == "F":
    p = (62.1*a)-44.7
    print(f"Seu peso ideal é {p}kg.")
elif s == "M":
    p = (72.7*a)-58
    print(f"Seu peso ideal é {p}kg.")
else:
    print("Digite um sexo válido!")
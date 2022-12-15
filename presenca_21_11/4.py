# 14. Write a Python program that accepts a string and calculate the number of digits and letters.

palavra = input("Insira uma palavra: ")
d=l=0

for c in palavra:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass

print(f"Letras: {l}")
print(f"Dígitos: {d}")

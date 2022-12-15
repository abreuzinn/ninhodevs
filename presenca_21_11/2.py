# 2. Write a Python program to convert temperatures to and from celsius, fahrenheit.

temp = input("Insira a escala da temperatura que você deseja converter (C ou F): ")

if temp == "C":
    tc = int(input("Insira o valor da temperatura: "))
    print(f"{tc}°C são {(tc*1.8)+32:.0f}°F.")

elif temp == "F":
    tf = int(input("Insira o valor da temperatura:"))
    print(f"{tf}°F são {(tf-32)/1.8:.0f}°C.")
else:
    print("Escala de temperatura inválida.")

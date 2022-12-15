# 9. Write a Python program to get the Fibonacci series between 0 to 50.
# nesse voce escolhe ate onde deseja calcular

x,y=0,1
z = int(input("Insira até onde deseja calcular uma sequência Fibonacci: "))

while y<=z:
    print(y)
    x,y = y,x+y
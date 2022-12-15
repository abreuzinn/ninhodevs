# 43. Write a Python program to create the multiplication table (from 1 to 10) of a number.

n = int(input("Insira um número de 1 a 10 para calcular a tabuada: "))

if (n>=1) and (n<=10):
    print(f"""Tabuada de {n}:

{n} x 1 = {n*1}
{n} x 2 = {n*2}
{n} x 3 = {n*3}
{n} x 4 = {n*4}
{n} x 5 = {n*5}
{n} x 6 = {n*6}
{n} x 7 = {n*7}
{n} x 8 = {n*8}
{n} x 9 = {n*9}
{n} x 10 = {n*10}
""")
else:
    print("Insira um número de 1 a 10!")
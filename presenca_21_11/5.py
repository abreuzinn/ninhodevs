# 6. Write a Python program to check a triangle is equilateral, isosceles or scalene.

print("Insira a largura dos 3 lados de um triângulo: ")
x = input("x: ")
y = input("y: ")
z = input("z: ")

if x == y == z:
    print("O triângulo é equilátero.")
elif x==y or y==z or z==x:
    print("O triângulo é isósceles.")
else:
    print("O triângulo é escaleno.")
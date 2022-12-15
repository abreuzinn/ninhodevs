# 3. Write a Python program to guess a number between 1 to 9.

import random

numero, adiv = random.randint(1, 10), 0

while numero != adiv:
    adiv = int(input('Adivinhe um número de 1 a 10: '))
print('Você adivinhou!')

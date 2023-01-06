# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import os
os.system("cls")

import random 

k = int(input("Enter K: "))

for i in range(k, 0, -1):
    x = random.randint(-10, 10)
    if x > 0:
        print(f'+ {x}x^{i}', end=' ')
    elif x == 0:
        print(end='')
    else:
        print(f'{x}x^{i}', end=' ')

print(random.randint(-10, 10))
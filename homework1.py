# Пользователь вводит число, нужно вывести чило pi с заданной точностью(БЕЗ БИБЛИОТЕК/МОДУЛЕЙ)

import os
os.system("cls")

a = int(input('Enter numb: '))
k = 0
pi = 0

for k in range(0, 1000):
    pi += (1 / 16 ** k) * ((4 / (8 * k + 1)) - (2 / (8 * k + 4)) - (1 / (8 * k + 5)) - (1 / (8 * k + 6)))

print(round(pi, a))
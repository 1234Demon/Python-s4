# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import os
os.system("cls")

list_numb = [1, 2, 10, 5, 2, 10, 1, 3, 4, 1]

list_uniq = []

for list_numb in list_numb:
    if list_numb not in list_uniq:
        list_uniq.append(list_numb)
    
print(list_uniq)
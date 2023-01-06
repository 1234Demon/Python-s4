# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

import os
os.system("cls")

n = int(input('Enter N: '))
k = 2
b = 0

while n != 1:
    while n % k == 0 :
        n = n / k
        b += 1
    if b != 0:
        print(k, '^', b)
    b = 0
    k += 1

# print(n != 1)
# print(n%2)
# print(n!=k)
# print(n%k)
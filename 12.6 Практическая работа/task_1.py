print('Задача 1. Сумма чисел')

# Напишите функцию summa_n,
# которая принимает одно целое положительное число N 
# и выводит сумму всех чисел от 1 до N включительно.
# 
# Пример работы программы:
# Введите число: 5
# 
# Я знаю, что сумма чисел от 1 до 5 равна 15

import math

def summa_number(number):
  sum_number = math.fsum(range(1, number + 1))
  print("Я знаю, что сумма чисел от 1 до", str(number), "равна", str(int(sum_number)))

number = int(input("Введите число: "))  
summa_number(number)

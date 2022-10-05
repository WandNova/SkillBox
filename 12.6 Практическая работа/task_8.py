print('Задача 8. НОД')

#Напишите функцию, вычисляющую наибольший общий делитель двух чисел

def maxCom_div(number_1, number_2):
  max_div = 1
  for div in range(1, number_1 + 1):
    if number_1 % div == 0 and number_2 % div == 0:
      max_div = div
  print("\nНаибольший общий делитель чисел:", max_div)

number_1 = int(input("Введите первое число: "))
number_2 = int(input("Введите второе число: "))
maxCom_div(number_1, number_2)

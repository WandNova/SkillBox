print('Задача 10. Яма')


# В одной компьютерной текстовой игре рисуются всяческие элементы ландшафта.
#
# Напишите программу,
# которая получает на вход число N и выводит на экран числа в виде “ямы”:

# Введите число: 5
# 
# 5........5
# 54......45
# 543....345
# 5432..2345
# 5432112345

number = int(input("Введите натуральное число большее 1: "))
for line in range(number):
  temp = number - line - 1
  for col in range(number, temp, - 1):
    print(col, end = "")
  print("." * temp * 2, end = "")
  for col in range(temp + 1, number + 1):
    print(col, end = "")
  print()
  
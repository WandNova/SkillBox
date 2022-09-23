print('Задача 2. Лестница')

# Пользователь вводит число N.
# Напишите программу, которая выводит такую “лесенку” из чисел:

# Введите число: 5
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

number = int(input("Введите N: "))
for line in range(1, number + 1):
  for column in range(number, number - line, - 1):
    print(line, end = " ")
  print()

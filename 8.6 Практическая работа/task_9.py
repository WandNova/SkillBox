print('Задача 9. Выражение')


# Дано число x.
# Напишите программу для вычисления следующего выражения 

# ((x-1)(x-3)(x-7)…(x-63)/
# ((x-2)(x-4)(x-8)…(x-64)) 

number = int(input("Введите число X: "))
numerator = 1
denominator = 1
for check in range(1, 7):
  numerator *= (number - (2 ** check - 1))
  denominator *= (number - 2 ** check) 
if denominator == 0:
  print("Ошибка")
else:
  print("Результат:", numerator / denominator)
print('Задача 8. Сумма ряда')

# Дано натуральное число n.
# Напишите программу для вычисления следующей суммы ряда (начиная с единицы)

# S = 1 - 1/2 + 1/4 - 1/8 + … (-1)**N * 1/2**N 

number = int(input("Введите число X: " ))
total = 0
for check in range(number + 1):
  expression = (-1)**check * 1 / 2**check
  total += expression
  print(check)
print(total)
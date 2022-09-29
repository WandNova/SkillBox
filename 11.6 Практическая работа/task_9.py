print('Задача 9. Уравнение')

# Даны действительные коэффициенты a, b, c,
# при этом a≠0. 
# Решите квадратное уравнение ax^2+bx+c=0 и выведите все его корни.
# 
# Если уравнение имеет два корня,
# выведите два корня в порядке возрастания,
# если один корень — выведите одно число, 
# если нет корней — не выводите ничего

import math

coef_a = float(input("Введите a: "))
coef_b = float(input("Введите b: "))
coef_c = float(input("Введите c: "))
discriminant = pow(coef_b, 2) - 4 * coef_a * coef_c
if discriminant == 0:
  print(- coef_b / (2 * coef_a))
elif discriminant > 0:
  print((- coef_b + math.sqrt(discriminant)) / (2 * coef_a))
  print((- coef_b - math.sqrt(discriminant)) / (2 * coef_a))
else:
  print("Нет действительных корней.")

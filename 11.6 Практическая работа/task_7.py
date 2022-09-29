print('Задача 7. Ход конём')


# В рамках разработки шахматного ИИ стоит новая задача.
# По заданным вещественным координатам коня
# и второй точки программа должна определить может ли конь ходить в эту точку.
# 
# Используйте как можно меньше конструкций if и логических операторов.
# Обеспечьте контроль ввода.

# Введите местоположение коня:
# 0.071
# 0.118
# Введите местоположение точки на доске:
# 0.213
# 0.068
# Конь в клетке (0, 1). Точка в клетке (2, 0).
# Да, конь может ходить в эту точку.

import math

distance_const = math.sqrt(pow(2 - 0, 2) + pow(0 - 1, 2)) # расст. мжд тчк и конём, т.к. по условию не должно быть лишних if
print("Введите местоположение коня:")
horse_x = float(input())
horse_y = float(input())
print("Введите местоположение точки на доске:")
point_x = float(input())
point_y = float(input())
if 0.000 <= horse_x <= 0.800 and 0.000 <= horse_y <= 0.800 and 0.000 <= point_x <= 0.800 and 0.000 <= point_y <= 0.800:
  point_int_x = int(point_x * 10)
  point_int_y = int(point_y * 10)
  horse_int_x = int(horse_x * 10)
  horse_int_y = int(horse_y * 10)
  print("Конь - в клетке (", end='')
  print(horse_int_x, end=', ')
  print(horse_int_y, end=')')
  print(". Точка - в клетке (", end='')
  print(point_int_x, end=', ')
  print(point_int_y, end=').\n')  
  distance = math.sqrt(pow(point_int_x - horse_int_x, 2) + pow(point_int_y - horse_int_y, 2))
  if distance == distance_const:
    print("Дa, конь может ходить в точку.")
  else:
    print("Нет, конь не может ходить в точку.")
else:
  print("Неверный ввод.")

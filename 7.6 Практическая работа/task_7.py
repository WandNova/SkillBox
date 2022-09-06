print('Задача 7. Отрезок')

# Напишите программу,
# которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль 
#среднее арифметическое всех чисел из отрезка [a; b], которые кратны числу 3.

number_1 = int(input("Введите первое число: "))
number_2 = int(input("Введите второе число: "))
total = 0
count = 0
for segment_number in range(number_1, number_2 + 1):
  if segment_number % 3 == 0:
    total += segment_number
    count += 1
print("Cреднее арифметическое всех чисел из отрезка ["+str(number_1)+"; "+str(number_2)+"], которые кратны числу 3:", total / count)
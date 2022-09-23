print('Задача 7. Наибольшая сумма цифр')

# Вводится N чисел. 
# Среди натуральных чисел, которые были введены, 
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.

count = int(input("Введите N: "))
max = 0
saved = 0
for each in range(count):
  print("Введите", each + 1, "натуральное число:", end = " ")
  number = int(input())
  temp = number
  summ = 0
  while number != 0:
    summ += number % 10
    number //= 10
  if summ > max:
    max = summ
    saved = temp
print("Наибольшей суммой цифр", max, "обладает число", saved)
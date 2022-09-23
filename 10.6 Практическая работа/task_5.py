print('Задача 5. Простые числа')


#Напишите программу,
#которая считает количество простых чисел в заданной последовательности 
#и выводит ответ на экран.

counter = 0
count = int(input("Введите размер последовательности: "))
for number in range(1, count + 1):
  print("Введите", number, "число:", end = " ")
  to_test = int(input())
  if to_test == 1:
    counter += 1
    continue
  is_prime = True
  for divider in range(2, to_test):
    if to_test % divider == 0:
      is_prime = False
      break
  if is_prime:
    counter += 1
print("Количество простых чисел:", counter)

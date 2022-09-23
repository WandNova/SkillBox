print('Задача 6. Сумма факториалов')

# Напишите программу,
# которая запрашивает у пользователя число N
# и находит сумму факториалов 1! + 2! + 3! +... + N! 

summ = 1
number = int(input("Введите N: "))
for boundary in range(2, number + 1):
  product = 1 
  for factor in range(2, boundary + 1):
    product *= factor
  summ += product
print("Сумма факториалов равна:", summ)

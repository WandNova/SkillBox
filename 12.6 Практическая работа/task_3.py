print('Задача 3. Апгрейд калькулятора')

# Степан, как и большая часть населения планеты,
# для расчёта суммы и разности чисел использует калькулятор.
# 
# Однако в работе ему нужно
# делать не только  обычные действия вроде сложения и вычитания,
# а делать что-то вручную он уже устал.
# 
# Поэтому Степан решил немного расширить функциональность своего калькулятора.
# 
# Напишите программу,
# которая спрашивает у пользователя число и действие, 
# которое нужно с ним сделать: 
# вывести сумму его цифр,
# вывести максимальную цифру или вывести минимальную цифру. 
# 
# Каждое действие оформите в виде отдельной функции, 
# а основную программу зациклите.

def summ():
  print("\n")
  number = int(input("Введите число: "))
  summ_number = 0
  while number > 0:
    summ_number += number % 10
    number = number // 10
  print(f"Сумма цифр числа равна {summ_number}") 

def max_number():
  print("\n")
  num = int(input("Введите число: "))
  max_number_b = number % 10
  while number > 0:
    number = number // 10
    if max_number_b < number % 10:
      max_number_b = number % 10
  print("Максимальная цифра в числе равна", max_number_b)

def min_number():
  print("\n")
  number = int(input("Введите число: "))
  min_number_b = number % 10
  while number > 0:
    number = number // 10
    if number == 0:
      break
    if min_number_b > number % 10:
      min_num_b = number % 10
  print("Минимальная цифра в числе равна", min_number_b)

def calc():
  action = int(input("Выберите действие (1 - вывести сумму цифр числа, 2 - вывести максимальную цифру числа, 3 - вывести минимальную цифру числа): "))
  if action == 1:
    summ()
    print("\n")
    calc()
  elif action == 2:
    max_number()
    print("\n")
    calc()
  else:
    min_number()
    print("\n")
    calc()

calc()

print('Задача 5. Счастливый билетик')

# В старину, когда даже в столице билеты в общественном транспорте выдавали контролёры,
# существовало поверье:
# если на билете сумма первых трёх цифр в номере билета равна сумме последних трёх,
# то это к удаче.
#
# Напишите программу,
# которая получала бы на входе номер билета из четного количества цифр
# и выводила, счастливый это билет или нет.
# К примеру, билеты 666 666 и 252 135 — счастливые,
# а 123 456 — нет.

number = int(input("Введите номер билета: "))
number_cout = 1
first_3 = 0
second_3 = 0
formula = number // (1000000 // 10**number_cout) % 10
while number_cout <= 6:
  if number_cout <= 3:
    first_3 += formula
    number_cout += 1
  elif number_cout <= 6:
    second_3 += formula
    number_cout += 1
if first_3 == second_3:
  print("Билет счастливый!")
else:
  print("Билет обычный")
  
print('Задача 6. Успеваемость в классе')

# В классе N человек.
# Каждый из них получил за урок по информатике оценку: 3, 4 или 5, двоек сегодня не было. 
# 
# Напишите программу, 
# которая получает список оценок - N чисел - и выводит на экран сообщение о том, 
# кого сегодня больше: отличников, хорошистов или троечников.

students = int(input("Введите количество учеников в классе: "))
excellent = 0
good = 0
three = 0
for cout in range(1, students + 1):
  estimates = int(input("Введите отценку ученика 3, 4 или 5: "))
  if estimates == 5:
    excellent += 1
  elif estimates == 4:
    good += 1
  else:
    three += 1
if (excellent > good) and (excellent > three):
  print("Сегодня больше отличников!")
elif (good > excellent) and (good > three):
  print("Сегодня больше хорошистов")
else:
  print("Сегодня больше троечников")
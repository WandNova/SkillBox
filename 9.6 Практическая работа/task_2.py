print('Задача 2. Я стал новым пиратом!')

#Старому капитану необходимо пополнить команду.
# Но попадут на его корабль только достойные! 
# Он отобрал 10 человек и те, кто из них крикнет слово “Карамба”, попадут на борт.
# 
# Пользователь вводит 10 слов. 
# 
# Напишите программу,
# которая определяет, сколько из них совпадают со словом “Карамба”.

total = 0

for cycle in range(10):
  text = input("Введите слово: ")
  if text == "карамба":
    total += 1

print("Набраных пиратов: ", total)
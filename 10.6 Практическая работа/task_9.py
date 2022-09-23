print('Задача 9. Пирамидка 2')


# Напишите программу,
# которая получает на вход количество уровней пирамиды и выводит их на экран,

# Пример:
# 
#             1
#          3     5
#       7     9     11
#    13    15    17    19
# 21    23    25    27    29

size = int(input("Введите число уровней пирамиды: "))
for level in range(1, size + 1):
  count = int((2*1 + (level - 1)) / 2 * level)
  An = 1 + 2 * (count - level)
  print("\t" * (size - level), end = "")
  print(An, end = "\t\t")
  
  for number in range(1, level):
    An = 1 + 2 * (count + number - level)
    print(An, end = "\t\t")
  print()
  
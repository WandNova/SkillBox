print('Задача 9. В обратном порядке')

# Реализуйте программу,
# которая получает на вход четырёхзначное число и выводит его на экран в обратном порядке.
# Само число при этом изменять нельзя, то есть нужно обойтись без переприсваивания.
# Однако можно использовать сколько угодно переменных.
# Пример ввода: 1234.
# Пример вывода: 4321.

number = int(input("Введите любое четырёхзначное число: "))
digit_1 = number // 1000
digit_2 = number // 100 % 10
digit_3 = number // 10 % 10
digit_4 = number % 10
print(digit_4)
print(digit_3)
print(digit_2)
print(digit_1)
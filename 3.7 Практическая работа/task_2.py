print('Задача 2. Финансовый отчёт')

# Наде дали задание сформировать финансовый отчёт за последние 20 лет по полугодиям. 
# Нужно сумму дохода первых двух кварталов поделить на сумму последних двух кварталов, 
# чтобы понять динамику роста или падения дохода. И так за каждый год. 
# 
# Надя решила, 
# что быстрее будет написать простую программу, которая сделает всё за неё.
# 
# 
# Запросите у пользователя четыре числа.
# Отдельно сложите первые два и отдельно вторые два.
# Разделите первую сумму на вторую.
# Выведите результат на экран.

profit_Q1 = int(input("Введите сумму дохода за 1 квартал: "))
profit_Q2 = int(input("Введите сумму дохода за 2 квартал: "))
profit_Q3 = int(input("Введите сумму дохода за 3 квартал: "))
profit_Q4 = int(input("Введите сумму дохода за 4 квартал: "))
sum_half_1 = (profit_Q1 + profit_Q2)
sum_half_2 = (profit_Q3 + profit_Q4)
print("Итого за 1 полугодие: ", sum_half_1)
print("Итого за 2 полугодие: ", sum_half_2)
print("Разница в доходах: ", sum_half_1 // sum_half_2)
print('Задача 9. Недоделка')

# Вы пришли на работу в контору по разработке игр,
# целевая аудитория которых - дети и их родители.
# 
# У прошлого программиста было задание
# сделать две игры в одном приложении, чтобы пользователь мог выбирать одну из них.
# 
# Однако программист, на место которого вы пришл
# и, перед увольнением не успел сделать эту задачу и оставил только небольшой шаблон проекта.
# 
# Используя этот шаблон,
# реализуйте игры «Камень, ножницы, бумага» и «Угадай число».
# 
# Правила игры «Камень, ножницы, бумага»:
# программа запрашивает у пользователя строку
# и выводит победил он или проиграл.
# 
# Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.
# 
# Правила игры “Угадай число”:
# программа запрашивает у пользователя число до тех пор, пока он его не отгадает.

import random

def rock_paper_scissors():
  program = random.randint(1, 3)
  if program == 1:
    program = "камень"
  elif program == 2:
    program = "ножницы"
  else:
    program = "бумага"
  human = input("Выберите: камень, ножницы, бумага?: ")
  if (program == "камень" and human == "бумага") or (program == "ножницы" and human =="камень") or (program == "бумага" and human =="ножницы"):
    print("Вы победили, робот выбрал -", program, "!")
  elif program == human:
    print("Робот выбрал то же самое, играем снова!")
    print()
    rock_paper_scissors()
  elif human != "камень" or "ножницы" or "бумага":
    print("Ошибка ввода!")
    rock_paper_scissors()
  else:
    print("Вы проиграли, робот выбрал -", program, "!")
  print()
  mainMenu()
#Здесь будет игра "Камень, ножницы, бумага"

def guess_the_number():
  print("Приветствую Вас в игре - «Угадай число или умри!»")
  computer = random.randint(1, 100)
  human = int(input("Угадайте число от 1 до 100: "))
  attempt = 0
  while human != computer:
    attempt += 1
    if human < computer:
      human = int(input("Загаданное число больше, попробуйте снова: "))
    else:
      human = int(input("Загаданное число меньше, попробуйте снова: "))
  print("Число угадано за", attempt, "попыток!")  
  print()
  mainMenu()
    #Здесь будет игра "Угадай число"

def mainMenu():
  print("Давайте выберем игру!")
  player = (input("1 - «Камень, ножницы, бумага», 2 - «Угадай число», если не хотите играть нажмите - 3: "))
  print()
  if player == "1":
    rock_paper_scissors()
  elif player == "2":
    guess_the_number()
  elif player == "3":
    print ("До свидание!")
  else:
    print ("Ошибка ввода")
    mainMenu()
  #Здесь главное меню игры
    
mainMenu()

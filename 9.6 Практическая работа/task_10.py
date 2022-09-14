print('Задача 10. Метод бутерброда')

# Секретное агентство «Super-Secret-no» решило
# для шифрования переписки своих сотрудников использовать «метод бутерброда».
# Сначала буквы слова нумеруются в таком порядке:
# первая буква получает номер 1,
# последняя буква - номер 2,
# вторая – номер 3,
# предпоследняя – номер 4, потом третья … и так для всех букв (см. рисунок).
# Затем все буквы записываются в шифр в порядке своих номеров.
# 
# Например, слово «sandwich» зашифруется в «shacnidw».
# 
# К сожалению, программист «Super-Secret-no», написал только программу шифрования и уволился.
# И теперь агенты не могут понять, что же они написали друг другу. Помогите им.
# 
# Пример:
# Введите зашифрованное сообщение: shacnidw
# Расшифрованное сообщение: sandwich
#          1   3   5   7   8   6   4   2
# Слово: | s | a | n | d | w | i | c | h |
#
# Шифр:  | s | h | a | c | n | i | d | w |
word = input("Введите зашифрованное сообщение: ")
# word_decod = ""
# decoding = ""
# for symbol in word:
#   print(symbol,"1")
#   word_decod = word.replace(symbol,"")
#   decoding += word_decod[0]
#   print(decoding)
# print(decoding)
left = ''
right = ''
max_len = len(word) - 1
for i, chr in enumerate(word):
  pos = i * 2
  if pos > max_len:
    pos = pos - max_len
    if max_len % 2 == 0:
      pos -= 1
    right = word[pos] + right
  else:
    left += word[pos]
print(left + right)
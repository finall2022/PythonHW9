""" Создайте программу для игры в ""Крестики-нолики"".

Пример интерфейса:

   |   | 0
-----------
   |   |
-----------
   | X |
Ввод можно реализовать через введение двух чисел (номеров строки и столбца). """

import emoji


def reverse(n):
   if n == '0':
      return('X')
   if n == 'x' or n == 'X':
      return('0')


def fillcell():
   row1 = ''.join(line1)
   row2 = ''.join(line2)
   row3 = ''.join(line3)
   top1 = ''.join(top)
   print(top1)
   print(f, row1, f)
   print(f, row2, f)
   print(f, row3, f)
   print(top1)


fill_ = emoji.emojize(":white_large_square:")
line1 = [fill_, fill_, fill_]
line2 = [fill_, fill_, fill_]
line3 = [fill_, fill_, fill_]

f = emoji.emojize(':collision:')
top = [f, f, f, f, f, f]
fillcell()
err1 = emoji.emojize(":index_pointing_up:")
err2 = emoji.emojize(":red_exclamation_mark:")
i = 1
correct = ('x', 'X', '0')
coord = (1, 2, 3)
n = str(input('Введите X или 0: '))
while n not in correct:
   n = str(input('Введите X или 0: '))

if n == '0':
   fc = emoji.emojize(':blue_circle:')
if n == 'x' or n == 'X':
   fc = emoji.emojize(':cross_mark_button:')

print(f'Первый ход за {fc}')
while i < 10:
   y = int(input('Введите номер строки от 1 до 3: '))
   x = int(input('Введите номер столбца от 1 до 3: '))
   if 0 < x <= 3 and 0 < y <= 3:
      if y == 1:
         line = line1
         if line[x-1] == fill_:
            if n == '0':
               line[x-1] = emoji.emojize(':blue_circle:')
            if n == 'x' or n == 'X':
               line[x-1] = emoji.emojize(':cross_mark_button:')
            i += 1
            temp = n
            n = reverse(temp)
         else:
            print(f'{err1} Ячейка занята')
      elif y == 2:
         line = line2
         if line[x-1] == fill_:
            if n == '0':
               line[x-1] = emoji.emojize(':blue_circle:')
            if n == 'x' or n == 'X':
               line[x-1] = emoji.emojize(':cross_mark_button:')
            i += 1
            temp = n
            n = reverse(temp)
         else:
            print(f'{err1} Ячейка занята')
      elif y == 3:
         line = line3
         if line[x-1] == fill_:
            if n == '0':
               line[x-1] = emoji.emojize(':blue_circle:')
            if n == 'x' or n == 'X':
               line[x-1] = emoji.emojize(':cross_mark_button:')
            i += 1
            temp = n
            n = reverse(temp)
         else:
            print(f'{err1} Ячейка занята')
   else:
      print(f'{err2}Неверные координаты, повторите ввод')
   
   fillcell()
   
   if n == '0':
      fc = emoji.emojize(':blue_circle:')
   if n == 'x' or n == 'X':
      fc = emoji.emojize(':cross_mark_button:')
   print(f'Теперь ход за {fc}')

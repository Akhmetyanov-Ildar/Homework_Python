
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# my_text = 'Напишите абв напиабв програбвмму программу, удаляющую из \
#     этого абв текста все вабвс слова, содерабващие содержащие "абв"'


# def del_some_words(my_text):
#     my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
#     return " ".join(my_text)


# my_text = del_some_words(my_text)
# print(my_text)

# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются
# сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# import random

# greeting = ('Здравствуйте! Вас приветствует игра "Забери все конфеты!" '
#             'Основные правила игры: '
#             'Нам будет дано некоторое количество конфет, '
#             'за один ход мы можем взять не более определённого количества, '
#             'о котором мы с вами договоримся.'
#             'Итак, начнём!')


# messages = ['Ваша очередь брать конфеты', 'возьмите конфеты',
#             'сколько конфет возьмёте?', 'берите, не стесняйтесь', 'Ваш ход']


# def play_game(n, m, players, messages):
#     count = 0
#     if n % 10 == 1 and 9 > n > 10:
#         letter = 'а'
#     elif 1 < n % 10 < 5 and 9 > n > 10:
#         letter = 'ы'
#     else:
#         letter = ''
#     while n > 0:
#         print(f'{players[count%2]}, {random.choice(messages)}')
#         move = int(input())
#         if move > n or move > m:
#             print(
#                 f'Это слишком много, можно взять не более {m} конфет{letter}, у нас всего {n} конфет{letter}')
#             attempt = 3
#             while attempt > 0:
#                 if n >= move <= m:
#                     break
#                 print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
#                 move = int(input())
#                 attempt -= 1
#             else:
#                 return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
#         n = n - move
#         if n > 0:
#             print(f'Осталось {n} конфет{letter}')
#         else:
#             print('Все конфеты разобраны.')
#         count += 1
#     return players[not count % 2]


# print(greeting)

# player1 = input(
#     'Давайте познакомися. Первый игрок, как к Вам можно обращаться?\n')
# player2 = input('Второй игрок, и Вы представьтесь, пожалуйста\n')
# players = [player1, player2]

# n = int(input('Сколько конфет будем разыгрывать?\n '))
# m = int(input('Сколько максимально будем брать конфет за один ход?\n '))

# winer = play_game(n, m, players, messages)
# if not winer:
#     print('У нас нет победителя.')
# else:
#     print(
#         f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!')


# Создайте программу для игры в ""Крестики-нолики"".
# import re


# print("*" * 10, "Крестики-нолики v1.0", "*" * 10)

# board = list(range(1, 10))


# def draw_board(board):
#     print("-"*13)
#     for i in range(3):
#         print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
#         print("-" * 13)


# def take_input(player_token):
#     valid = False
#     while not valid:
#         player_answer = input("Куда поставим: " + player_token + "? ")

#         try:
#             player_answer = int(player_answer)
#         except:
#             print("Некорректный ввод. Вы уверены, что ввели число?")
#             continue
#         if player_answer >= 1 and player_answer <= 9:
#             if (str(board[player_answer - 1]) not in "XO"):
#                 board[player_answer - 1] = player_token
#                 valid = True
#             else:
#                 print("Эта клетка уже занята")

#         else:
#             print("Введите число от 1 да 9")


# def check_win(board):
#     win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
#                  (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
#     for each in win_coord:
#         if board[each[0]] == board[each[1]] == board[each[2]]:
#             return board[each[0]]
#     return False


# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#             take_input("X")
#         else:
#             take_input("0")
#         counter += 1

#         if counter > 4:
#             tmp = check_win(board)
#             if tmp:
#                 print(tmp, "Ты выйграл!")
#                 win = True
#                 break
#         if counter == 9:
#             print("Ничья!!!")
#             break

#     draw_board(board)


# main(board)


# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# with open('42_RLE1_decoded.txt', 'r') as data:
#     my_text = data.read()


# def encode_rle(ss):
#     str_code = ''
#     prev_char = ''
#     count = 1
#     for char in ss:
#         if char != prev_char:
#             if prev_char:
#                 str_code += str(count) + prev_char
#             count = 1
#             prev_char = char
#         else:
#             count += 1
#     return str_code


# str_code = encode_rle(my_text)
# print(str_code)

# with open('42_RLE2_encoded.txt', 'r') as data:
#     my_text2 = data.read()


# def decoding_rle(ss: str):
#     count = ''
#     str_decode = ''
#     for char in ss:
#         if char.isdigit():
#             count += char
#         else:
#             str_decode += char * int(count)
#             count = ''
#     return str_decode


# str_decode = decoding_rle(my_text2)
# print(str_decode)

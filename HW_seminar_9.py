# Игра крестики-нолики

# from tkinter import font
# from turtle import color, width
# from numpy import size
# import pygame
# import sys


# def check_win(mas, sign):
#     zeroes = 0
#     for row in mas:
#         zeroes += row.count(0)
#         if row.count(sign) == 3:
#             return sign
#     for col in range(3):
#         if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
#             return sign
#     if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
#         return sign
#     if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
#         return sign
#     if zeroes == 0:
#         return 'Piece'
#     return False


# pygame.init()
# size_block = 100
# margin = 15
# width = heigth = size_block*3 + margin * 4

# size_window = (width, heigth)
# screen = pygame.display.set_mode(size_window)
# pygame.display.set_caption("Крестики-нолики")

# black = (0, 0, 0)
# red = (255, 0, 0)
# green = (0, 255, 0)
# white = (255, 255, 255)
# mas = [[0]*3 for i in range(3)]
# query = 0
# game_over = False

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit(0)
#         elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
#             x_mouse, y_mouse = pygame.mouse.get_pos()
#             col = x_mouse // (size_block + margin)
#             row = y_mouse // (size_block + margin)
#             if mas[row][col] == 0:
#                 if query % 2 == 0:
#                     mas[row][col] = 'x'
#                 else:
#                     mas[row][col] = 'o'
#                 query += 1
#         elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
#             game_over = False
#             mas = [[0]*3 for i in range(3)]
#             query = 0
#             screen.fill(black)

#     if not game_over:
#         for row in range(3):
#             for col in range(3):
#                 if mas[row][col] == 'x':
#                     color = red
#                 elif mas[row][col] == 'o':
#                     color = green
#                 else:
#                     color = white
#                 x = col*size_block + (col+1)*margin
#                 y = row * size_block + (row + 1) * margin
#                 pygame.draw.rect(screen, color, (x, y, size_block, size_block))
#                 if color == red:
#                     pygame.draw.line(screen, white, (x+5, y+5),
#                                      (x+size_block - 5, y+size_block - 5), 3)
#                     pygame.draw.line(screen, white, (x+size_block - 5, y+5),
#                                      (x+5, y+size_block - 5), 3)
#                 elif color == green:
#                     pygame.draw.circle(
#                         screen, white, (x+size_block//2, y+size_block//2), size_block//2-3, 3)
#     if (query-1) % 2 == 0:
#         game_over = check_win(mas, 'x')
#     else:
#         game_over = check_win(mas, 'o')

#     if game_over:
#         screen.fill(black)
#         font = pygame.font.SysFont('stxingkai', 80)
#         text1 = font.render(game_over, True, white)
#         text_rect = text1.get_rect()
#         text_x = screen.get_width()/2 - text_rect.width/2
#         text_y = screen.get_height()/2 - text_rect.height/2
#         screen.blit(text1, [text_x, text_y])

#     pygame.display.update()

# 3. Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь,
# в котором каждый элемент списка является и ключом и значением.
# Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях.

# Для решения воспользуемся генератором словарей (dict comprehension).
# def to_dict(lst):
#     return {element: element for element in lst}

# print(to_dict([1, 2, 3, 4]))
# print(to_dict(['grey', (2, 17), 3.11, -4]))


# 4. Иван решил создать самый большой словарь в мире. Для этого он придумал
# функцию biggest_dict(**kwargs), которая принимает неограниченное количество
# параметров «ключ: значение» и обновляет созданный им словарь my_dict, состоящий
# всего из одного элемента «first_one» со значением «we can do it». Воссоздайте эту функцию.

# my_dict = {'first_one': 'we can do it'}


# def biggest_dict(**kwargs):
#     my_dict.update(**kwargs)


# biggest_dict(k1=22, k2=31, k3=11, k4=91)
# biggest_dict(name='Елена', age=31, weight=61, eyes_color='grey')
# print(my_dict)


# 5. Дана строка в виде случайной последовательности чисел от 0 до 9.
# Требуется создать словарь, который в качестве ключей будет принимать
# данные числа (т. е. ключи будут типом int), а в качестве значений – количество
# этих чисел в имеющейся последовательности. Для построения словаря создайте функцию
# count_it(sequence), принимающую строку из цифр. Функция должна возвратить словарь
# из 3-х самых часто встречаемых чисел.

# def count_it(sequence):
#     # При помощи генератора создаем словарь, где ключом выступает уникальный элемент строки,
#     # а значением - его частота (вычисляется методом count())
#     num_frequency = {int(item): sequence.count(item) for item in sequence}

#     # Сортируем словарь по значениям в порядке возрастания.
#     # Для этого методом items() формируем пары “(ключ, значение)” в виде кортежей
#     # по всем элементам словаря. Т. к. нужно сортировать по значениям, берем второй
#     # элемент кортежей. В результате получим список из кортежей “(ключ, значение)”
#     sorted_num_frequency = sorted(
#         num_frequency.items(), key=lambda element: element[1])

#     # Возвращаем последние 3 элемента списка, т. е. кортежи с
#     # самыми большими значениями второй компоненты, которые преобразовываем в словарь
#     return dict(sorted_num_frequency[-3:])


# # Тесты
# print(count_it('1111111111222'))
# print(count_it('123456789012133288776655353535353441111'))
# print(count_it('007767757744331166554444'))

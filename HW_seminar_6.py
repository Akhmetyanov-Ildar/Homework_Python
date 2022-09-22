# Задача 41: Напишите программу вычисления арифметического
# выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
# - Добавьте возможность использования скобок, меняющих приоритет операций.
#    *Пример:*
#     1+2*3 => 7;
#     (1+2)*3 => 9;

# import re


# actions = {
#     "^": lambda x, y: str(float(x)**float(y)),
#     "*": lambda x, y: str(float(x) * float(y)),
#     "/": lambda x, y: str(float(x) / float(y)),
#     "+": lambda x, y: str(float(x) + float(y)),
#     "-": lambda x, y: str(float(x) - float(y))
# }

# priority_reg_exp = r"\((.+?)\)"
# action_reg_exp = r"(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)"


# def my_eval(expresion: str) -> str:

#     while (match := re.search(priority_reg_exp, expresion)):
#         expresion: str = expresion.replace(
#             match.group(0), my_eval(match.group(1)))

#     for symbol, action in actions.items():
#         while (match := re.search(action_reg_exp.format(symbol), expresion)):
#             expresion: str = expresion.replace(
#                 match.group(0), action(*match.groups()))

#     return expresion


# exp = "1+2*3"
# print(my_eval(exp), eval(exp))


# Задача 43: Дана последовательность чисел.
# Получить список уникальных элементов заданной последовательности.

# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

# my_list = [1, 2, 3, 5, 1, 5, 3, 10]


# def get_unic(my_list):
#     unic = []
#     for i in range(len(my_list)):
#         if my_list[i] not in my_list[i+1::] and my_list[i] not in my_list[:i-1:]:
#             unic.append(my_list[i])
#     return unic


# print(get_unic(my_list))

# Вычислить число c заданной точностью d
# Пример:
# # - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
# from decimal import Decimal

# n = int(input("Введите число: "))
# d = str(input("Введите степень точности: "))

# d = Decimal(str(d)).as_tuple().exponent*(-1)

# print(f'{n:.{d}f}')


# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

# n = int(input("Введите число: "))
# for i in range(1, n+1):
#     if (n % i == 0):
#         print(i)


# Задайте последовательность чисел.
# Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.

# lst = list(map(int, input("Введите числа через пробел:\n").split()))
# print(f"Исходный список: {lst}")
# new_lst = []
# [new_lst.append(i) for i in lst if i not in new_lst]
# print(f"Список из неповторяющихся элементов: {new_lst}")

# Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


# def write_file(st):
#     with open('file33.txt', 'w') as data:
#         data.write(st)


# def rnd():
#     return random.randint(0, 101)


# def create_mn(k):
#     lst = [rnd() for i in range(k+1)]
#     return lst


# def create_str(sp):
#     lst = sp[::-1]
#     wr = ''
#     if len(lst) < 1:
#         wr = 'x = 0'
#     else:
#         for i in range(len(lst)):
#             if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
#                 wr += f'{lst[i]}x^{len(lst)-i-1}'
#                 if lst[i+1] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 2 and lst[i] != 0:
#                 wr += f'{lst[i]}x'
#                 if lst[i+1] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 1 and lst[i] != 0:
#                 wr += f'{lst[i]} = 0'
#             elif i == len(lst) - 1 and lst[i] == 0:
#                 wr += ' = 0'
#     return wr


# k = int(input("Введите натуральную степень k = "))
# koef = create_mn(k)
# write_file(create_str(koef))

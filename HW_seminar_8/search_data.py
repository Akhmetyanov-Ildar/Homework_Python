import time


def txt_input(rad):
    f = open('data.txt', 'r', encoding="utf-8")
    num = f.readlines()
    user_list = []
    for i in num:
        raw_test = i.split()
        user_data = {'LastName': raw_test[0],
                     'Name': raw_test[1], 'Number': raw_test[2]}
        user_list.append(user_data)
    f.close()
    return user_list


def search():
    list = txt_input('data.txt')
    request = input('Кого искать?: ')

    t = True
    for i in list:
        if i['LastName'] == request or i['Name'] == request or i['Number'] == request:
            print(*i.values())
            t = False
    if t:
        print('Нет такого usera')

    input('нажмите Enter для продолжения')


def print_all(list):
    for i in list:
        print(i)
        time.sleep(0.2)
    input('Введите Enter')

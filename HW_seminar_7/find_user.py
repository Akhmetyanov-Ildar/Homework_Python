
def search(list):
    request = input('Введите что нибудь для поиска: ')

    t = True
    for i in list:
        if i['LastName'] == request or i['Name'] == request or i['Number'] == request or i['Email'] == request or i['Sity'] == request or i['Sex'] == request:
            print(*i.values())
            t = False
    if t:
        print('Нет такого usera')

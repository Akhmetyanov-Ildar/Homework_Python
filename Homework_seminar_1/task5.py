# Напишите программу для. проверки
# истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input('Введите X: '))
y = int(input('Введите Y: '))
z = int(input('Введите Z: '))

print((not (x or y or z)) == (not x and not y and not z))

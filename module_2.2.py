first = int(input('Введите число: '))
second = int(input('Введите число: '))
third = int(input('Введите число: '))
if first == second and first == second and first == third:
    print(3)
elif first == second or first == third:
    print(2)
elif first != second and first != third and first != third:
    print(0)
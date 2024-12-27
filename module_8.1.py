def add_everything_up(a, b):
    try:
        result = a + b
        if isinstance(result, float):
            return f"{result:.3f}"
    except TypeError:
        return str(a) + str(b)
    else:
       return a + b


# Примеры использования
print(add_everything_up(123.456, 'строка'))  # Вывод: 123.456строка
print(add_everything_up('яблоко', 4215))  # Вывод: яблоко4215
print(add_everything_up(123.456, 7))

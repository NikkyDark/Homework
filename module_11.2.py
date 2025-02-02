def introspection_info(obj):
    # Получаем тип объекта
    obj_type = type(obj).__name__

    # Получаем атрибуты объекта
    attributes = dir(obj)

    # Получаем методы объекта
    methods = [attr for attr in attributes if callable(getattr(obj, attr, None))]

    # Получаем модуль, к которому объект принадлежит (с проверкой)
    module = getattr(type(obj), '__module__', 'builtins')

    # Создаем словарь с информацией об объекте
    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module
    }

    return info


# Пример работы функции
number_info = introspection_info(42)
print(number_info)

string_info = introspection_info("Hello, world!")
print(string_info)

list_info = introspection_info([1, 2, 3])
print(list_info)

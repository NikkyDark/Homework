class IncorrectWinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


class Car:
    def __init__(self, model, win, numbers):
        self.model = model
        self._win = self._is_valid_win(win)
        self._numbers = self._is_valid_numbers(numbers)

    def _is_valid_win(self, win_number):
        if not isinstance(win_number, int):
            raise IncorrectWinNumber('Некорректный тип win номера')
        if win_number < 1000000 or win_number > 9999999:
            raise IncorrectWinNumber('Неверный диапазон для win номера')

    def _is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длинна номера')
        return numbers


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectWinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectWinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectWinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')

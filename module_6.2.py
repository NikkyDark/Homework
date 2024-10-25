class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self._model = model
        self._engine_power = engine_power
        self._color = color

    def get_model(self):
        return f"Модель: {self._model}. "

    def get_horse_power(self):
        return f"Мощность двигателя: {self._engine_power}."

    def get_color(self):
        return f"Цвет: {self._color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horse_power())
        print(self.get_color())
        print(f"Владелец: {self.owner}. ")

    def set_color(self, new_color):
        if new_color.lower() in map(str.lower, self.__COLOR_VARIANTS):
            self._color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, model, color, engine_power):
        super().__init__(owner, model, engine_power, color)


vehicle1 = Sedan('Vasya Pupkin', 'Mercedes CLA AMG', 'black', 650)

vehicle1.print_info()

vehicle1.set_color('Green')
vehicle1.set_color('PINK')
vehicle1.engine_power = 2000
vehicle1.owner = 'Avdotiy Petrovich'

vehicle1.print_info()

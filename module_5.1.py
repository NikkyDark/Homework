class House:
    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors

    def go_to(self, new_floor):
        if 0 < new_floor <= self.number_of_floors:
            for floor in range(1, new_floor+1):
                print(floor)
        else:
            print('Такого этажа не вуществует')


h1 = House('ЖК Эльбрус', 30)
h2 = House('Ближние Раздоры', 25)
h1.go_to(5)
h2.go_to(27)

class House:
    def __init__(self, name, number_of_floors):

        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):

        if 0 < new_floor <= self.number_of_floors:

            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")

    def __len__(self):

        return (self.number_of_floors)

    def __str__(self):

        return (f"Название: {self.name}, кол-во этажей: {self.number_of_floors}")

a = House('ЖК Эльбрус', 30)

a1 = House('ЖК Эльбрус', 10)

a2 = House('ЖК Акация', 20)

a.go_to(30)
a.go_to(32)

#__str__
print(a1)
print(a2)

#__len__
print(len(a1))
print(len(a2))
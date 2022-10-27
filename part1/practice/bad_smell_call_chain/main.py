# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов


class City:
    def __init__(self, population):
        self.population = population

    def population(self):
        return self.population


class Person:
    def __init__(self, room_number):
        self.room_number = room_number

    def get_person_room(self):
        return self.room_number


person = Person(23)
print(person.get_person_room())

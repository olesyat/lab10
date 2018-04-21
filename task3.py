from ecoo import River, Ecosystem, Animal
import random


class Bear(Animal):
    def __init__(self):
        super().__init__()
        self._age = random.randint(1, 10)
        self._birth = 2


class Fish(Animal):
    def __init__(self):
        super().__init__()
        self._age = random.randint(1, 5)
        self._birth = 7


class Otter(Animal):
    def __init__(self):
        super().__init__()
        self._age = random.randint(1, 12)
        self._birth = 3


class River3(River):
    CHOICES = [Bear(), Fish(), Otter(), None]

    def __init__(self):
        super().__init__()

    def fight(self, animal1, animal2):
        if animal1 == None:
            return [animal2]
        elif animal2 == None:
            return [animal1]

        elif str(animal1) == str(animal2):
            if animal1._sex != animal2._sex:
                Ecosystem.BUFFER.append(animal2)
                if str(animal2) == 'Bear':
                    new_animal = Bear()
                if str(animal2) == 'Fish':
                    new_animal = Fish()
                if str(animal2) == 'Otter':
                    new_animal = Otter()
                for i in range(animal2._birth):
                    Ecosystem.BUFFER.append()
                return [animal1]
            else:
                if animal1._power == animal2._power:
                    return animal1 if animal1._age < animal2._age else animal2
                elif animal1._power > animal2._power:
                    return [animal1]
                else:
                    return [animal2]
        elif str(animal2) == 'Bear':
            return [animal2]
        elif str(animal1) == 'Bear':
            return [animal1]

        elif str(animal2) == 'Otter' and str(animal1) == 'Fish':
            return [animal2]
        elif str(animal1) == 'Otter' and str(animal2) == 'Fish':
            return [animal1]

river = River3()
print(river.act())
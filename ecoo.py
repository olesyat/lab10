import random


class Ecosystem:
    BUFFER = []
    SYSTEM = {'Bear': [], 'Fish': [], 'Otter': []}

    def __init__(self, river):
        self.river = river

    def start_stimulation(self):
        for j in range(1):
            self.river = self.river.move()
            print('river after move', self.river)

            for i in range(len(self.river)):
                while len(self.river[i]) > 1:
                    self.river[i] = self.river.fight(self.river[i][0], self.river[i][1])
        print('river after fight', self.river)


class Animal:
    def __init__(self):
        self._power = random.randint(1, 10)
        self._age = random.randint(1, 10)
        self._sex = random.choice([True, False])
        self._birth = self.KIDS

    def __str__(self):
        return type(self).__name__


class Bear(Animal):
    KIDS = 2


class Fish(Animal):
    KIDS = 7


class Otter(Animal):
    KIDS = 3


class River(list):
    def __init__(self):
        self.size = random.randint(1, 10)
        self.choices = self.CHOICES
        for i in range(self.size):
            animal = random.choice(self.choices)
            if animal:
                self.append([animal])
            else:
                self.append([])

    def move(self):
        new_river = [[] for i in range(self.size)]
        print(self)
        moves = [-1, 0, 1]
        for i in range(self.size):
            a = random.choice(moves)
            try:
                new_river[(i + a) % self.size].append(self[i][0])
            except IndexError:
                pass

        for i, e in enumerate(new_river):
            self[i] = e

        return self

    def fight(self):
        pass


class River1(River):
    CHOICES = [str(Bear()), str(Fish()), None]

    def fight(self, animal1, animal2):
        if animal1 == None:
            return [str(animal2)]
        elif animal2 == None:
            return [str(animal1)]
        elif animal1 == animal2:
            for i in range(2):
                Ecosystem.BUFFER.append(animal2)
            return [str(animal1)]
        elif animal1 != animal2:
            return [str(Bear())]


a = Ecosystem(River1())
a.start_stimulation()

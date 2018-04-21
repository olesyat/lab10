import random


class Ecosystem:
    BUFFER = []
    SYSTEM = {'Bear': [], 'Fish': [], 'Otter': []}

    def __init__(self, river):
        self.river = river

    def start_stimulation(self):
        print('river before', self.river)
        for j in range(1):
            self.river = self.river.move()
            print('river after move', self.river)

            for i in range(len(self.river)):
                while len(self.river[i]) > 1:
                    self.river[i] = self.river.fight(self.river[i][0], self.river[i][1])
        print('river after fight', self.river)
        print("BUFFER", self.BUFFER)

    def __str__(self):
        ecosys = []
        for element in self.river:
            if element:
                ecosys.append("'" + type(element[0]).__name__[0] + str(element[0]._power) + str(element[0]._sex) + str(element[0]._age) + "'")
            else:
                ecosys.append("'    '")

        return ' '.join(ecosys)

class Animal:
    def __init__(self):
        self._power = random.randint(1, 10)
        self._sex = random.choice([True, False])

    def __str__(self):
        return type(self).__name__

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


class River(list):
    def __init__(self):
        self.size = random.randint(1, 10)
        self.choices = self.CHOICES
        for i in range(self.size):
            animal = random.choice(self.choices)
            if animal:
                if animal == 'Bear':
                    self.append([Bear()])
                elif animal == 'Fish':
                    self.append([Fish()])
                elif animal == 'Otter':
                    self.append([Otter()])
            else:
                self.append([])

    def move(self):
        new_river = [[] for i in range(self.size)]
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






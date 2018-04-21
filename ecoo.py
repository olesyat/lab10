import random


class Ecosystem:
    def __init__(self, river):
        self.river = river



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
        self = new_river
        return self


class River_1(River):
    CHOICES = [str(Bear()), str(Fish()), None]


class River_3(River):
    CHOICES = [Bear(), Fish(), Otter(), None]


a = River_1()
print(a.move())

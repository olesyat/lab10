import random

class Ecosystem:
    def __init__(self, river):
        self.river = river

    def move(self):
        pass


class River(list):
    def __init__(self):
        self.size = random.randint(1, 100)
        self.choices = [Bear(), Fish(), None]
        for i in range(self.size):
            self.append([random.choice(self.choices)])

    def pr(self):
        return self

class Animal:
    def __init__(self):
        self._power = random.randint(1, 10)
        self._age = random.randint(1, 10)
        self._sex = random.choice(True, False)
        self._birth = self.KIDS

class Bear(Animal):
    KIDS = 2

class Fish(Animal):
    KIDS = 7

class Otter(Animal):
    KIDS = 3


a = River()
print(a.pr)
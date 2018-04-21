import random
import copy


class Ecosystem:
    BUFFER = []

    def __init__(self, river):
        self.river = river


class Animal:
    def __init__(self):
        self._power = random.randint(1, 10)
        self._sex = random.choice([True, False])
        # використовується тільки в task3.py
        # self._age = random.randint(1, 10)
        # self._birth = self.KIDS

    def __str__(self):
        return type(self).__name__


class River(list):
    def __init__(self):
        self.size = random.randint(1, 10)
        self.choices = self.CHOICES
        for i in range(self.size):
            self.append([random.choice(self.choices)])

    def move(self):
        new_river = [[] for i in range(self.size)]
        moves = [-1, 0, 1]
        for i in range(self.size):
            a = random.choice(moves)
            new_river[(i + a) % self.size].append(self[i][0])
        self = new_river
        return new_river

    def act(self):
        moved = self.move()
        print("moved: ", moved)
        for j in range(len(moved)):
            self[j] = self.interaction(moved[j])
        return self

    def interaction(self, lst):
        if len(lst) < 2:
            return lst
        else:
            for i in range(1, len(lst)):
                lst[0] = self.fight(lst[0], lst[i])
            return lst[0]

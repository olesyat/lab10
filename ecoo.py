import random
import copy


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
            self.append([random.choice(self.choices)])

    def move(self):
        # new_river = copy.deepcopy(self)
        # moves = [-1, 0, 1]
        # print(new_river)
        # for i in range(self.size):
        #     a = random.choice(moves)
        #     if len(new_river[i]) > 1:
        #         new_river[i % self.size + a].append(new_river[i][0])
        #     else:
        #         new_river[i % self.size + a].append(new_river[i])
        #     print("moving:", a, ",step", i, new_river)
        #
        # return new_river
        new_river = [[] for i in range(self.size)]
        print(self)
        moves = [-1, 0, 1]
        for i in range(self.size):
            a = random.choice(moves)
            print(a, i, "what happ: ", new_river[(i + a) % self.size], (self[i][0]))
            new_river[(i + a) % self.size].append(self[i][0])
            #print(a, new_river)
        self = new_river
        return new_river


class River_1(River):
    CHOICES = [str(Bear()), str(Fish()), None]


class River_3(River):
    CHOICES = [str(Bear()), str(Fish()), str(Otter()), None]


a = River_1()
print(a.move())

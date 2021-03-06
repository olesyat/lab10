import random


class Ecosystem:
    '''The class to represent the ecosystem'''
    BUFFER = []
    SYSTEM = {'Bear': [], 'Fish': [], 'Otter': []}
    START_BUF = -1

    def __init__(self, river):
        self.river = river

    def start_stimulation(self):
        '''method to do the simulation'''
        for j in range(2):

            print('river before', self)
            self.river = self.river.move()

            print('river after move', self)

            for i in range(len(self.river)):
                if not len(self.river[i]):
                    self.buffer_to_river(i)

                while len(self.river[i]) > 1:
                    self.river[i] = self.river.fight(self.river[i][0],
                                                     self.river[i][1])

            for i in range(Ecosystem.START_BUF):
                if not len(self.river[1]):
                    self.buffer_to_river(i)

            Ecosystem.START_BUF = -1
            if len(Ecosystem.BUFFER):
                Ecosystem.BUFFER.clear()

            print('river after fight', self)
            print("BUFFER", self.BUFFER)

    def buffer_to_river(self, i):
        '''method to add the animal from buffer'''
        try:
            new = Ecosystem.BUFFER.pop()
            self.river[i] = [new]
            if Ecosystem.START_BUF == -1:
                Ecosystem.START_BUF = i
        except IndexError:
            pass

    def sixty_percent(self):
        '''method to control the population'''
        lst = [len(self.SYSTEM['Bear']), len(self.SYSTEM['Fish']),
               len(self.SYSTEM['Otter'])]
        all = sum(lst)
        max_ = max(lst)
        max_1 = ['Bear', 'Fish', 'Otter']
        i = 0
        while max_ > all * 0.6:
            print("ПЕРЕНАСЕЛЕННЯ")
            print(self.SYSTEM)
            new = self.SYSTEM[max_1[lst.index(max_)]]
            ages = [element._age for element in new]
            if i % 2 == 0:
                remove_ = max(ages)
            else:
                remove_ = min(ages)

            lets_kill = new[ages.index(remove_)]
            new.remove(lets_kill)
            self.SYSTEM[max_1[lst.index(max_)]] = new

            # removing from river

            for el in self.river:
                if el:
                    if el[0] is lets_kill:
                        el = []
            i += 1
            lst = [len(self.SYSTEM['Bear']), len(self.SYSTEM['Fish']),
                   len(self.SYSTEM['Otter'])]
            all = sum(lst)
            max_ = max(lst)
            print("Natural selection killing ", lets_kill)
        else:
            pass
        print(self.SYSTEM)

    def __str__(self):
        ecosys = []
        for element in self.river:
            if element:
                for i in range(len(element)):
                    ecosys.append("'" + type(element[i]).__name__[i] + str(
                        element[i]._power) + str(element[i]._sex) + str(
                        element[i]._age) + "'")

            else:
                ecosys.append("'    '")

        return ' '.join(ecosys)

class Animal:
    '''Parent class for all the animals in ecosystem'''
    def __init__(self):
        self._power = random.randint(1, 10)
        self._sex = random.choice([True, False])

    def __str__(self):
        return type(self).__name__


class Bear(Animal):
    '''Class to represent a Bear'''
    def __init__(self):
        super().__init__()
        self._age = random.randint(1, 10)
        self._birth = 2


class Fish(Animal):
    '''Class to represent a Fish'''
    def __init__(self):
        super().__init__()
        self._age = random.randint(1, 5)
        self._birth = 7


class Otter(Animal):
    '''Class to represent an Otter'''
    def __init__(self):
        super().__init__()
        self._age = random.randint(1, 12)
        self._birth = 3


class River(list):
    '''Parent class for all the types of the rivers'''
    def __init__(self):
        self.size = random.randint(1, 10)
        self.choices = self.CHOICES
        for i in range(self.size):
            animal = random.choice(self.choices)
            if animal:
                if animal == 'Bear':
                    animal_choice = Bear()
                    Ecosystem.SYSTEM[str(animal_choice)].append(animal_choice)
                    self.append([animal_choice])
                elif animal == 'Fish':
                    animal_choice = Fish()
                    Ecosystem.SYSTEM[str(animal_choice)].append(animal_choice)
                    self.append([animal_choice])
                elif animal == 'Otter':
                    animal_choice = Otter()
                    Ecosystem.SYSTEM[str(animal_choice)].append(animal_choice)
                    self.append([animal_choice])
            else:
                self.append([])

    def move(self):
        '''method to move the animals'''
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
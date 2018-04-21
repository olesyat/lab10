from ecoo import River, Ecosystem, Animal


class Bear(Animal):
    pass


class Fish(Animal):
    pass


class River2(River):
    CHOICES = [Bear(), Fish(), None]

    def __init__(self):
        super().__init__()

    def fight(self, animal1, animal2):
        if animal1 == None:
            return [animal2]
        elif animal2 == None:
            return [animal1]
        elif animal1 == animal2:
            if animal1._sex == animal2._sex:
                return [animal1] if animal1._power > animal2._power else [
                    animal2]
            else:
                new_animal = Bear() if str(animal1) == 'Bear' else Fish()
                Ecosystem.BUFFER.append(animal2)
                Ecosystem.BUFFER.append(new_animal)
                return [animal1]
        elif animal1 != animal2:
            return [animal1] if str(animal1) == 'Bear' else [animal2]


river = River2()
print(river)
print(river.act())

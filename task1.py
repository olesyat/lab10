from ecoo import River, Ecosystem, Bear, Fish


class River1(River):
    CHOICES = [str(Bear()), str(Fish()), None]

    def __init__(self):
        super().__init__()


    def fight(self, animal1, animal2):
        if animal1 == None:
            return [str(animal2)]
        elif animal2 == None:
            return [str(animal1)]
        elif animal1 == animal2:
            Ecosystem.BUFFER.append(animal2)
            return [str(animal1)]
        elif animal1 != animal2:
            return [str(Bear())]


river = River1()
print(river)
# print(river.move())
print(river.act())

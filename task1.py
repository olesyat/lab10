from ecoo import River, Ecosystem, Bear, Fish


class River1(River):
    CHOICES = ['Bear', 'Fish', None]

    def fight(self, animal1, animal2):
        if type(animal1) == type(animal2):
            Ecosystem.BUFFER.append(animal2)
            Ecosystem.BUFFER.append(Bear()) if str(animal1) == 'Bear' else Ecosystem.BUFFER.append(Fish())
            return [animal1]
        else:
            return [animal1] if str(animal1) == 'Bear' else [animal2]


a = Ecosystem(River1())
a.start_stimulation()
print(a)
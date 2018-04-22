from ecoo import River, Ecosystem, Bear, Fish


class River2(River):
    CHOICES = ['Bear', 'Fish', None]

    def fight(self, animal1, animal2):
        if type(animal1) == type(animal2):
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


a = Ecosystem(River2())
a.start_stimulation()

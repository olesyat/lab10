from ecoo import River, Ecosystem, Bear, Fish, Otter


class River3(River):
    CHOICES = ['Bear', 'Fish', 'Otter', None]

    def fight(self, animal1, animal2):
        if type(animal1) == type(animal2):
            if animal1._sex != animal2._sex:
                Ecosystem.BUFFER.append(animal2)
                if str(animal2) == 'Bear':
                    new_animal = Bear()
                if str(animal2) == 'Fish':
                    new_animal = Fish()
                if str(animal2) == 'Otter':
                    new_animal = Otter()
                for i in range(animal2._birth):
                    Ecosystem.SYSTEM[str(new_animal)].append([new_animal])
                    Ecosystem.BUFFER.append(new_animal)
                return [animal1]
            else:
                if animal1._power == animal2._power:
                    if animal1._age < animal2._age:
                        Ecosystem.SYSTEM[str(animal2)].remove(animal2)
                        return animal1
                    else:
                        Ecosystem.SYSTEM[str(animal1)].remove(animal1)
                        return animal2

                elif animal1._power > animal2._power:
                    Ecosystem.SYSTEM[str(animal2)].remove(animal2)
                    return [animal1]
                else:
                    Ecosystem.SYSTEM[str(animal1)].remove(animal1)
                    return [animal2]

        elif str(animal2) == 'Bear':
            Ecosystem.SYSTEM[str(animal1)].remove(animal1)
            return [animal2]
        elif str(animal1) == 'Bear':
            Ecosystem.SYSTEM[str(animal2)].remove(animal2)
            return [animal1]

        elif str(animal2) == 'Otter' and str(animal1) == 'Fish':
            Ecosystem.SYSTEM[str(animal1)].remove(animal1)
            return [animal2]
        elif str(animal1) == 'Otter' and str(animal2) == 'Fish':
            Ecosystem.SYSTEM[str(animal2)].remove(animal2)
            return [animal1]

a = Ecosystem(River3())
print(a)
a.start_stimulation()
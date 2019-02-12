class Animal_A(object):
    __a = 1

    def voice(self):
        return "animal A"

    def __private(self):
        pass


class Animal_C(Animal_A):
    pass
    # def voice(self):
    #     return "animal C"


class Animal_D(Animal_A):
    def voice(self):
        return "animal D" + super().voice()


class Dog(Animal_C, Animal_D):
    pass

a = Animal_A()
d1 = Dog()
d2 = Dog()
# d1 + d2

# print(d.voice())

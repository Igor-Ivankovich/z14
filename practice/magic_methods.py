class MyClass:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"Object {self.number}"

    def __repr__(self):
        return f"<repr class {self.number}>"

    def __eq__(self, other):
        return self.number == other.number

    def __gt__(self, other):
        return self.number > other.number

    def __ge__(self, other):
        return self.number >= other.number

    def __lt__(self, other):
        return self.number < other.number

    def __neg__(self):
        self.number = -self.number
        return self

    def __pos__(self):
        pass

    def __abs__(self):
        pass

    def __add__(self, other):
        self.number += other
        return self

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)


m1 = MyClass(3)
m2 = MyClass(3)

print(str(m1))  # __str__
print(repr(m2))  # __repr__

if m1 == m2:  # __eq__
    print("==")
else:
    print("!=")

m1 = MyClass(4)
m2 = MyClass(3)

print(m1 >= m2)  # __ge__

m1 = -m1  # __neg__

m3 = m1 + 2  # __add__
m4 = 2 + m1  # __radd__

m4 += 3  # __iadd__
print(m4)

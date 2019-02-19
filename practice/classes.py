import random


class User:
    adult_age = 18

    def __init__(self, first_name, age, last_name=None):
        self._first_name = first_name
        self._last_name = last_name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not (1 < value < 100):
            print('Wrong age')
        else:
            self._age = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value[::-1]

    @first_name.deleter
    def first_name(self):
        self._first_name = None

    def is_adult(self):
        return self._age >= self.adult_age

    @staticmethod
    def get_adult_age():
        return 18

    @classmethod
    def get_adult_age_v2(cls):
        return cls.adult_age

    @classmethod
    def generate_users(cls, count):
        for i in range(count):
            yield cls(f"First_{i}", random.randint(User.adult_age, 100))


u1 = User("User1", 12, "Last1")
u2 = User("User2", 19)
print(u1.is_adult(), u2.is_adult())

users = list(User.generate_users(8))
print(len(users))
for user in users:
    print(user.first_name, user.age)

print("#" * 10)
print(u1.first_name)
u1.first_name = 'New name'
u1.age = 150
print(u1.age)
print(u1.first_name)
del u1.first_name
print('Deleter', u1.first_name)

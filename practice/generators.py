import random


class RandomGenerator:
    def __init__(self, n):
        self.n = n
        self.index = 0

    def __next__(self):
        if self.index >= self.n:
            raise StopIteration
        self.index += 1
        return random.random()

    def __iter__(self):
        return self

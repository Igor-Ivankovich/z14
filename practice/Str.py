class Str(str):
    def __truediv__(self, other):
        return Str(self[:len(self) // other])

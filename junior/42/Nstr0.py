class Nstr(str):
    def __sub__(self, other):
        return self.replace(other, '')

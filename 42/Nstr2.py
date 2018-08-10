class Nstr():
    def __init__(self, s):
        self.ascii = 0

        for c in s:
            self.ascii += ord(c)

    def __add__(self, other):
        return self.ascii + other.ascii

    def __sub__(self, other):
        return self.ascii - other.ascii

    def __mul__(self, other):
        return self.ascii * other.ascii

    def __truediv__(self, other):
        return self.ascii / other.ascii

    def __floordiv__(self, other):
        return self.ascii // other.ascii
    

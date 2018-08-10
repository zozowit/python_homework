class Nstr:
    def __lshift__(self, other):
        return self[other:] + self[: other]

    def __rshift__(self, other):
        return self[-other:] + self[: -other]

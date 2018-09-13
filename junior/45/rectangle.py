class Rectangle:
    def __init__(self, w = 0, h = 0):
        self.w = w
        self.h = h

    def __setattr__(self, name, value):
        if name == 'square':
            self.w = value
            self.h = value
        else:
            super().__setattr__(name, value)
            self.__dict__[name] = value

    def getArea(self):
        return self.w * self.h

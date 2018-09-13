import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, A, B):
        self.A = A
        self.B = B

        self.len = math.sqrt((A.x - B.x)*(A.x - B.x) + (A.y - B.y) * (A.y - B.y))
        self.len = math.fabs(self.len)

    def getLen(self):
        return self.len
        
        

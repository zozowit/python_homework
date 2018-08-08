class Nint(int):
    def __new__(cls, x):
        t = type(x)
        
        if t == int:
            return x
        elif t == float:
            return int(x)
        elif t == str:
            ret = 0
            for c in x:
                ret += ord(c)

            return ret

class Nint(int):
    def __new__(cls, x):
        t = type(x)
        
        if t == str:
            ret = 0
            for c in x:
                ret += ord(c)

            return ret
        else:
            return int.__new__(cls, x)

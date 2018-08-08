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
=======
>>>>>>> 9a8d41513bf3cc7eede369a02b0e5a9602b89eb0

class TempProperty:
    def __init__(self, fget=None, fset=None, fdel=None):
            self.fget = fget
            self.fset = fset
            self.fdel = fdel
    def __get__(self, instance, owner):
            return self.fget(instance)
        
    def __set__(self, instance, value):
            return self.fset(instance, value)
        
    def __del__(self, instance):
            self.fdel(instance)
            
class Temperature:
    def __init__(self):
        self._c = None
        self._f = None
        
    def getC(self):
        return self._c

    def setC(self, c):
        self._c = c
        self._f = self._c * 1.8 + 32

    def delC(self):
        del self._c

    def getF(self):
        return self._f

    def setF(self, f):
        self._f = f
        self._c = (self._f - 32) / 1.8

    def delF(self):
        del self._f

    c = TempProperty(getC, setC, delC)
    f = TempProperty(getF, setF, delF)
        

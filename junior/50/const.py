class Const:
    def __setattr__(self, name, value):
        if name.isupper() is False:
            raise TypeError('常量名必须由大写字母组成！')
        elif hasattr(self, name) is True:
            raise TypeError('常量无法改变！')
        else:
            self.__dict__[name] = value

import sys
sys.modules[__name__] = Const()

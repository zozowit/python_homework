import pickle as pk
import os

class MyDes:
    def __init__(self, value, name=None):
        self.name = name
        self.value = value
        self.pf_name = name + '.pk'

        with open(self.pf_name, 'wb') as f:
            pk.dump(self.value, f)

    def __get__(self, instance, owner):
        print('正在获取变量:', self.name)
        with open(self.pf_name, 'rb') as f:
            return pk.load(f)

    def __set__(self, instance, value):
        print('正在修改变量：', self.name)
        self.value = value
        
        with open(self.pf_name, 'wb') as f:
            pk.dump(self.value, f)

    def __delete__(self, instance):
        print('正在删除变量：', self.name)
        os.remove(self.pf_name)

class Test:
	x = MyDes(10, 'x')
	y = MyDes(8.8, 'y')

	
test = Test()

test.x

test.y

test.x = 123

test.x = 1.23    
        

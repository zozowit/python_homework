import time as t

class MyDes:
    f_name = 'record.txt'

    def __init__(self, value, name=None):
        self.name = name
        self.value = value

    def __get__(self, instance, owner):
        print('正在获取变量:', self.name)
        cur_t = self._get_time()
        temp_s = '%s变量于北京时间%s 被读取, %s = %s\n'%(self.name, cur_t, self.name, str(self.value))
        self._store(temp_s)
        return self.value

    def __set__(self, instance, value):
        print('正在修改变量：', self.name)
        self.value = value

        cur_t = self._get_time()
        temp_s = '%s变量于北京时间%s 被修改, %s = %s\n'%(self.name, cur_t, self.name, str(self.value))
        self._store(temp_s)

    def __delete__(self, instance):
        print('正在删除变量：', self.name)
        print('哦~这个变量没法删除~')

    def _get_time(self):
        localtime = t.asctime(t.localtime(t.time()))
        return localtime

    def _store(self, line):
        f = open(MyDes.f_name, 'a')
        f.write(line)
        f.close()
        
class Test:
	x = MyDes(10, 'x')
	y = MyDes(8.8, 'y')

	
test = Test()

test.x

test.y

test.x = 123

test.x = 1.23

test.y = 'I love FishC.com'

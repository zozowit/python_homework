import random as r
import time

class Animal(object):
    

    def __init__(self, name, x, y):
        self.cur_pos = [0, 0] #x, y
        self.cur_pos[0] = r.randint(0, x)
        self.cur_pos[1] = r.randint(0, y)

        self.name = name

        print('New born:%s'%self.name)
        self.dump_attribute()

    def dump_attribute(self):
        
        print('=================================')
        print('name:%s'%self.name)
        print('current position: %s'%(str(self.cur_pos)))
        print('=================================')
       
class Fish(Animal):
    def get_fish_name(self):
        return self.name


class Turtle(Animal):
    def get_turtle_name(self):
        return self.name


def kill_zone():
    count = 0
    print('game start')
    t1 = Turtle(name = 'Turtle', x=10, y=10)
    f1 = Fish(name = 'Fish', x=10, y=10)

    print("t1 pos:[%s], f1 pos:[%s]"%(str(t1.cur_pos), str(f1.cur_pos)))

kill_zone()

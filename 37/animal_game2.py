import random as r
import time

class Animal:
    def __init__(self, name, x, y, power, direct, ability, sn):
        self.cur_pos = [0, 0] #x, y
        self.cur_pos[0] = r.randint(0, x)
        self.cur_pos[1] = r.randint(0, y)

        self.cur_power = power

        self.direct = r.randint(0, direct)

        self.m_ability = ability
        
        self.x_bound = [0, 0]
        self.y_bound = [0, 0]

        self.x_bound[1] = x
        self.y_bound[1] = y

        self.is_dead = False

        self.name = name

        self.sn = sn

        print('New born:%s-%d'%(self.name, self.sn))
        self.dump_attribute()

    def dump_attribute(self):
        
        print('=================================')
        print('name:%s-%d'%(self.name, self.sn))
        print('area:x[%d, %d], y[%d, %d]'
              %(self.x_bound[0], self.x_bound[1], self.y_bound[0], self.y_bound[1]))
        print('move ability: %d'%self.m_ability)
        print('current position: %s'%(str(self.cur_pos)))
        print('current power: %d'%(self.cur_power))
        print('current direction:%d'%self.direct)
        print('is dead: %d'%self.is_dead)
        print('=================================')

    def set_bound(x_min, x_max, y_min, y_max):
        x_bound[0] = x_min
        x_bound[1] = x_max
        y_bound[0] = y_min
        y_bound[1] = y_max

        print('set bound area:x[%d, %d], y[%d, %d]'
              %(self.x_bound[0], self.x_bound[1], self.y_bound[0], self.y_bound[1]))

    def set_power(self, power):
        self.cur_power = power
        print("set_power:%d"%power)

    def calc_next_move(self):
        return r.randint(1, self.m_ability)

    def calc_direct(self):
        cur_x = self.cur_pos[0]
        cur_y = self.cur_pos[1]

        x = self.x_bound
        y = self.y_bound

        #print('%s calc direction: cur[%d, %d], bound[%d, %d, %d, %d], direction:%d'%(self.name, cur_x, cur_y, x[0], x[1], y[0], y[1], self.direct))
        
        if cur_x < x[0]:
            self.direct = 3 # set from left to right
            self.cur_pos[0] = x[0] # reset x to min
            #print("3-direct=%d"%self.direct)
            
        elif cur_x > x[1]:
            self.direct = 2 # set to left
            self.cur_pos[0] = x[1]
            #print("2-direct=%d"%self.direct)
            
        elif cur_y < y[0]:
            self.direct = 0 # set to up
            self.cur_pos[1] = y[0]
            #print("0-direct=%d"%self.direct)
            
        elif cur_y > y[1]:
            self.direct = 1 # set to down
            self.cur_pos[1] = y[1]
            #print("1-direct=%d"%self.direct)

        #print('%s calc direction over: cur[%d, %d], bound[%d, %d, %d, %d], direction:%d'%(self.name, self.cur_pos[0], self.cur_pos[1], x[0], x[1], y[0], y[1], self.direct))

    def move(self):
        cur_x = self.cur_pos[0]
        cur_y = self.cur_pos[1]

        move = self.calc_next_move()
        
        if self.direct == 0: #move up
            cur_y += move
        if self.direct == 1: #move down
            cur_y -= move
        if self.direct == 2: #move left
            cur_x -= move
        if self.direct == 3: #move right
            cur_x += move

        self.cur_pos[0] = cur_x
        self.cur_pos[1] = cur_y
        #print('cur_pos[%d,%d][cur_x:%d,cur_y:%d]'%(self.cur_pos[0], self.cur_pos[1], cur_x, cur_y))

        self.calc_direct()

        self.cur_power -= 1

        print('%s move %d step to [%d, %d], direction=%d, power=%d'%(self.name, move, self.cur_pos[0], self.cur_pos[1], self.direct, self.cur_power))

    def is_dead(self):
        return self.is_dead

    def get_pos(self):
        return self.cur_pos
            
        
class Fish(Animal):
    def kill(self):
        self.is_dead = True
        print('kill')

class Turtle(Animal):
    def get_dead(self):
        if self.cur_power <= 0:
            self.is_dead = True

        return self.is_dead
    def eat(self):
        self.cur_power += 10


def mult_move(t_d, f_d):
    for each_t in t_d:
        t_d[each_t].move()

    for each_f in f_d:
        f_d[each_f].move()

def perform_kill(t_d, f_d):
    for each_t in list(t_d.keys()):
        cur_t = t_d[each_t]
        if cur_t.get_dead() is True:
            print('!!!!%s-%d die by hungry!!!'%(cur_t.name, cur_t.sn))
            t_d.pop(each_t)
            continue
        
        t_pos = cur_t.cur_pos
        for each_f in list(f_d.keys()):
            cur_f = f_d[each_f]
            if cur_f.cur_pos == cur_t.cur_pos:
                cur_f.kill()
                cur_t.eat()
                print('!!!!%s-%d kill by turtle%s!!!'%(cur_f.name, cur_f.sn, cur_t.name))
                f_d.pop(each_f)

def mult_kill_zone():
    count = 0
    t_d = {}
    f_d = {}

    t_num = int(input('请输入乌龟的个数：'))
    f_num = int(input('请输入鱼的个数：'))
    
    print('game start')

    for i in range(t_num):
        t_name = 'Turtle-%d'%(i)
        t1 = Turtle(name = t_name, x=10, y=10, power=100, direct=3, ability=2, sn = i)
        t_d[t_name] = t1


    for i in range(f_num):
        f_name = 'Fish-%d'%(i)
        f1 = Fish(name = f_name, x=10, y=10, power=999, direct=3, ability=1, sn = i)
        f_d[f_name] = f1

    while True:
        mult_move(t_d, f_d)

        perform_kill(t_d, f_d)

        time.sleep(0.01)
        count += 1
        print('Round %d'%count)

        if len(t_d) == 0:
            print('Fish win！！')
            break
        if len(f_d) == 0:
            print('Turtle win!!')
            break

    print('game over')

mult_kill_zone()

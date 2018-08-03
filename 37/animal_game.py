import random as r

class animal:
    m_ability = 0
    cur_pos = [0, 0] #x, y
    cur_power = 0
    direct = 0 #0 up, 1 down, 2 left, 3 right

    def __init__(self, x, y, power, direct, ability):
        self.cur_pos[0] = r.randint(0, x)
        self.cur_pos[1] = r.randint(0, y)

        self.cur_power = power

        self.direct = r.randint(0, direct)

        self.m_ability = ability

    def set_power(self, power):
        self.cur_power = power
        print("set_power:%d"%power)

    def calc_nex_move(self):
        return r.randint(1, m_ability)

    def get_direct(self, x, y):
        cur_x = self.cur_pos[0]
        cur_y = self.cur_pos[1]
        if cur_x < x[0]:
            self.direct = 3 # set to right
        if cur_x > x[1]:
            self.direct = 2 # set to left
        if cur_y < y[0]:
            self.diret = 0 # set to up
        if cur_y > y[1]:
            self.diret = 1 # set to down
    def change_direct(self):
        x = edge or y = edge and direct to oposit

    def move()
            

class Fish:

class Rectangle():
    heigh = 5.00
    width = 4.00

    def getRect(self):
        print("这个矩形的长是:%.2f, 宽是:%.2f"%(self.heigh, self.width))

    def setRect(self):
        print('请输入矩形的长和宽...')
        cur_h = input('长:')
        cur_w = input('宽:')

        self.heigh = float(cur_h)
        self.width = float(cur_w)

    def getArea(self):
        print(self.heigh * self.width)

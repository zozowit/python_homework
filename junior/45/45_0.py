class C:
    def __getattr__(self, name):
        print('该属性不存在')

    def __init__(self):
        self.x = 1
        self.y = 2

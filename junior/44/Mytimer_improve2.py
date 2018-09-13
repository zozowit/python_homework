import time as t

class MyTimer():
    def __init__(self, func, count=1000000):
        self.prompt = '未开始计时！'
        self.lasted = 0
        self.begin =  t.perf_counter()
        self.end =  t.perf_counter()
        self.count = count
        self.func = func

    def __str__(self):
        return self.prompt

    __repr__ = __str__

    def __add__(self, other):
        prompt = '总共运行了'
        prompt += str(self.lasted + other.lasted)

        return prompt

    def timing(self):
        temp_begin = t.process_time()
        for i in range(self.count):
            self.func
        temp_end = t.process_time()

        self.lasted = temp_end - temp_begin

        self.prompt = '总共运行了'

        self.prompt += str(self.lasted) + '秒'

    def start(self):
        print(t.process_time())
        self.begin = t.perf_counter()
        self.prompt = '提示：请先调用stop()停止计时'
        print('计时开始...')
        print(t.process_time())

    def stop(self):
        print(t.process_time())

        if not self.begin:
            print('提示，请先调用start()进行计时！')
        else:
            self.end = t.perf_counter()
            self._calc()
            print('计时结束！')
        print(t.process_time())

    def _calc(self):
        self.lasted = self.end - self.begin
        self.prompt = '总共运行了'

        self.prompt += str(self.lasted) + '秒'


        self.begin = 0
        self.end = 0

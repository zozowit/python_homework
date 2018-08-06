class Counter:
    instance_num = 0

    def __init__(self):
        Counter.instance_num += 1

    def __del__(self):
        Counter.instance_num -= 1

    def get_instance_num(self):
        print('instance num:%d'%Counter.instance_num)

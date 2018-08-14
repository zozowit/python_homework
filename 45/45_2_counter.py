class Counter:
    def __init__(self):
        self.counter = -1

    def __setattr__(self, name, value):
        super().__setattr__(name, value)
        super().__setattr__('counter', self.counter + 1)

    def __delattr__(self, name):
        super().__delattr__(name)
        super().__setattr__('counter', self.counter - 1)

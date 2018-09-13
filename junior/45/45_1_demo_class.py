class Demo:
    def __getattr__(self, name):
        super().__setattr__(name, 'FishC')

        return super().__getattribute__(name)

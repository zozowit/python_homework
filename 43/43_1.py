class Word(str):
    def __init__(self, value):
        self.len = len(self)
        print(self.len, value)
        str.__init__(self, value)

class myRevClass:
    def __init__(self, seq):
        self.seq = list(seq)
        self.index = len(self.seq)

    def __iter__(self):
        return self

    def __next__(self):
        self.index -= 1
        if self.index < 0:
            raise StopIteration
        
        #print(self.index, self.seq[self.index])
        return self.seq[self.index]

def myRev(data):
    l_data = list(data)
    while True:
        try:
            yield l_data.pop()
        except IndexError:
            raise StopIteration
        

for i in myRev('FishC'):
    print(i, end='')
    pass

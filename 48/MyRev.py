class MyRev:
    def __init__(self, seq):
        self.seq = []
        l_seq = list(seq)
        self._reversed(l_seq)

    def _reversed(self, seq):
        print('reverse', seq)
        seq.reverse()
        self.seq = seq
        print('get', self.seq)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = self.seq[0]
            del self.seq[0]
            return item
        except IndexError:
            raise StopIteration

myRev = MyRev('FishC')
for i in myRev:
    print(i, end='')

    

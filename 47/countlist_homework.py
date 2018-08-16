class CountList():
    def __init__(self, *args):
        self.values = [x for x in args]
        self.count = [0 for x in args]

    def __repr__(self):
        return str(self.values)

    def __str__(self):
        return str(self.values)

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        self.count[key] += 1

        return self.values[key]

    def __setitem__(self, key, value):
        self.count[key] += 1

        self.values[key] = value

    def __delitem__(self, key):
        self.count.remove(key)
        self.values.remove(key)
        

    def counter(self, key):
        return self.count[key]

    def append(self, value):
        self.values.append(value)
        self.count.append(0)

    def pop(self, key = -1):
        self.count.pop(key)
        return self.values.pop(key)

    def remove(self, value):
        key = self.values.index(value)
        self.values.remove(value)
        self.count.pop(key)

    def insert(self, key, value):
        self.values.insert(key, value)
        self.count.insert(key, 0)

    def clear(self):
        self.values.clear()
        self.count.clear()

    def reverse(self):
        self.values.reverse()
        self.count.reverse()



c1 = CountList(1, 3, 5, 7, 9)
c2 = CountList(2, 4, 6, 8, 10)

c1[1]
c2[1]
c1[1]+c2[2]







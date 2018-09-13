def getPrime(data = 2000000):
    for i in range(2, data):
        for j in range(2, i):
            if i%j == 0:
                break
        else:
            yield i

for i in getPrime():
    print(i, end=' ')

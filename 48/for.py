rg = range(5)
it = iter(rg)
while True:
    try:
        print(next(it))
    except StopIteration:
        break

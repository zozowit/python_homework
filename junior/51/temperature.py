def c2f(cel):
    fah = cel * 1.8 + 32
    return fah

def f2c(fah):
    cel =(fah - 32) / 1.8

    return cel

def test():
    print("test, 0 degree = %.2f hf"%c2f(0));
    print("test, 0 hf = %.2f degree"%f2c(0));

if __name__ == "__main__":
    test()

class C():
    def __init__(self, *args):
        print(*args, type(*args))
        print(args, type(args))
        
        if not args:
            print('并没有传入参数')
        else:
            print('传入了%d个参数，分别是:%s'%(len(args), str(args)))

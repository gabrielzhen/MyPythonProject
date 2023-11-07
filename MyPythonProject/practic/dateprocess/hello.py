import sys
def test():
    args=sys.argv
    if len(args)==1:
        print('hello world')
    elif len(args)==2:
        print('hello %s'%args[1])
    else:
        print('to manay arguments')

if __name__=='__main__':
    print('ok')
    test()
    print(sys.path)
else:
    print('Error')
def log(fun):
    def wrapper():
        print('call %s:'%fun.__name__) #获取函数的名称 并打印
        return fun()  #返回函数 并且执行函数
    return wrapper

@log
def now():
    print('2015-3-25')

now= log(now)
now()

import time,functools
def metric(funn):
    def wrapper(*args):
        print('%s executed in %s ms' % (funn.__name__,time.time()))
        return funn(*args)
    return wrapper

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
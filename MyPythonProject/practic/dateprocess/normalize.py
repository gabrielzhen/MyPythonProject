#利用高阶map函数实现规范英文单子大小写的功能
from functools import reduce
def normalize(name):
    a=name[0]
    b=name[1:]
    return(a.upper()+b.lower())
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

#利用高阶函数reduce实现乘积
def prod(lists):
    def multiply(x,y):
        return(x*y)
    return reduce(multiply,lists)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

#利用map和reduce把字符串转化为浮点数
def str2float(s):
    dot=int(s.index('.'))
    x,y,z=0,0,1
    for i in s[0:dot]:
        x=(int(i)+x)*10
    for i in s[dot+1:]:
        y=(int(i)+y)*10
        z=z*10
    return(x/10+y/10/z)
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')


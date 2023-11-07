#如果偶数 打印 number//2并返回值
#如果奇数 打印并返回3×number+1
#sing：用户输入一个数字 进行判断 知道函数返回1
#todo：定义函数
def collatz(num):
    if (num % 2)==0:
        print(num//2)
        return num//2
    else:
        print(3*num+1)
        return 3*num+1
##todo：调用函数 并循环判断
try:
    numb=int(input('Enter your number!'))
    coll=collatz(numb)
    while coll!=1:
        coll=collatz(coll)
except ValueError:
    print('Enter a wrong number!again')


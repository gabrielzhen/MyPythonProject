##递归算法
##案例：汉诺塔 
# 按照递归的思想  先吧其他的当做n-1和n 然后再利用两个盘子的算法进行实现
#一共三个柱子  一个当前柱子 一个目标柱子 一个缓存柱子
#然后利用递归思想调用自身 实现
def hano(n,A,B,C):
    if n==1 :
        print(A,'-->',C)
    else:
        hano(n-1,A,C,B)
        print(A,'-->',C)
        hano(n-1,B,A,C)

num=int(input('请输入盘子数量'))
hano(num,'A','B','C')
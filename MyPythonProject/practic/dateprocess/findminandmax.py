#利用迭代查找list中最小和最大的值 并返回tuple
def findMinAndMax(lists):
    if len(lists):
        minnum=lists[0]
        maxnum=lists[0]
        for childlist in lists:
            if minnum>childlist:
                minnum=childlist
            if maxnum<childlist:
                maxnum=childlist
        return (minnum,maxnum)
    else:
        return (None,None)
        
    
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

L1 = ['Hello', 'World', 18, 'Apple', None]
L2=[x.lower() for x in L1 if isinstance(x, str)]
print(L2)
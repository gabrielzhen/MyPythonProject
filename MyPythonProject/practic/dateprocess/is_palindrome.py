####高级函数筛选器filter使用
def not_empty(s):
    return s and s.strip()
g=filter(not_empty, ['A', '', 'B', None, 'C', '  '])
print(next(g))

##素数
#因为固定的列和列生成式 在没有异常抛出的时候不好判断下标溢出  所以使用生成器
##素数判断定义dc
# def _not_divisible(s):
#     return lambda x:x%s>0
# ##主函数
# def primes():
#     lists=(x for x in range (3,30))
#     while True:
#         first=next(lists)
#         lists=iter(filter(_not_divisible(first),list(lists)))
# primes()

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(L[1])
def sort_n(t):
    return(t[0])
def sort_s(t):
    return(t[1])
print(sorted(L,key=sort_n))
print(sorted(L,key=sort_s))

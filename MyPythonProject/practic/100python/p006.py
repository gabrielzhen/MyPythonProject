'''
Function Call: 函数调用：
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
Output: 输出：
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
Function Call: 函数调用：
'''
def f(s):
    l=s.split(' ')
    a,op,b=int(l[0]),l[1],int(l[2])
    c=eval(s)
    max_lenth=len(str(max(a,b)))+2

    r=[]
    r.append(str(a).rjust(max_lenth,' '))
    r.append(op+' '+str(c).rjust(max_lenth-2,' '))
    r.append('-'*max_lenth)
    r.append(str(c).rjust(max_lenth,' '))
    return r


def arithmetic_arranger(lists,show=False):
    if len(lists)>5:
        return "error too long"
    d=[]
    for l in lists:
        try:
            ps=f(l)
            d.append(ps)
        except Exception as e:
            print('have error')
            return str(e)
    arranged_problems=''
    n=3
    if show:
        n=4
    for i in range(n):
        for j in range(len(d)):
            if j==0:
                arranged_problems=arranged_problems+d[j][i]
            else:
                arranged_problems=arranged_problems+'   '+d[j][i]
            if i !=n-1:
                arranged_problems=arranged_problems+'\n'
    return arranged_problems
if __name__=='__mian__':
    a=arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])
    print(a)
# f("3 + 5")
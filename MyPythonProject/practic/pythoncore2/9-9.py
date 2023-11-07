# import os
# dir='C:\Python34\Lib'
# files=[i for i in os.listdir(dir) if i.endswith('.py')]
# for f in files:
#     fulldir=os.path.join(dir,f)
#     openfile=open(fulldir)
#!/usr/bin/env python

# def safe_float(obj):
#     try:
#         retval=float(obj)
#     except Exception , e:
#         retval=str(e)
#     return retval

# def main():
#     log=open('a.txt','w')
#     try:
#         ccfile=open('b.txt','r')
#     except IOError , e:
#         log.write('no this month')
#         log.close()
#         return
#     txns=ccfile.readlines()
#     ccfile.close()
#     total=0
#     log.write('account log:\n')
    
#     for eachtxn in txns:
#         result=safe_float(eachtxn)
#         if isinstance(result,float):
#             total+=result
#             log.write('data.....processing')
#         else:
#             log.write('ignored %s' % result)
#     log.close()
from operator import add,sub 
from random import randint,choice

# ops={'+':add,'-':sub}
# maxtrys=2

# def doprob():
#     op=choice('+-')
#     nums=[randint(1,10) for i in range(2)]
#     nums.sort(reverse=True)
#     ans=ops[op](*nums)
#     pr='%d %s %d='%(nums[0],op,nums[1])
#     oops=0
#     while True:
#         try:
#             if int(input(pr))==ans:
#                 print('correct')
#                 break
#             if oops==maxtrys:
#                 print('answer is %s%d'%(pr,ans))
#             else:
#                 print('incorrect... try again')
#                 oops+=1
#         except Exception as e:
#             print('this is error:%s'% e)

# def main():
#     while True:
#         print('begin')
#         print(doprob.__dir__)
#         doprob()
        

#         try :
#             opt=input('agin?[y]').lower()
#             if opt and opt[0]=='n':
#                 break
#         except Exception:
#             break
# if __name__=='__main__':
#     main()


#!/usr/lib/env python
# from time import ctime,sleep

# def tsfunc(fun):
#     # def wrapper():
#     #     print('[%s]%s() called'% (ctime(),fun.__name__))
#     #     return fun()
#     print('[%s]%s() called'% (ctime(),fun.__name__))
#     return fun

# @tsfunc
# def foo():
#     pass

# foo()
# def testit(func,*nkwarys,**kwarys):
#     try:
#         retval=func(*nkwarys,**kwarys)
#         result=(True,retval)
#     except Exception as diag:
#         result=(False,str(diag))
#     return result

# def test():
#     funcs=(int,float)
#     vals=(1234,12.34,'1234','12,34')

#     for eachfunc in funcs:
#         print ('_'*20)
#         for eachval in vals:
#             retval=testit(eachfunc,eachval)
#             if retval[0]:
#                 print('success%s',retval[1])
#             else:
#                 print('false%s',retval[1])

# if __name__=='__main__':
#     test()
# from decimal import Decimal
# print(Decimal(0.1))
# print(Decimal('0.1'))
# def foo():
#     return print ('in foo()')
# bar=foo
# print(type(bar))
# print(bar())
# print('--'*20)
# bar2=foo()
# print(type(bar2))
# print(bar2)
#闭包 可以用来计数，原理是counter返回一个inc函数，inc函数是累加的
# def counter(start=0):
#     count=[start]
#     def inc():
#         count[0]+=1
#         return count[0]
#     return inc

# def counter(start=0):
#     count=[start]
#     count[0]+=1
#     return count[0]


# c=counter
# print(type(counter()))
# print(id(c))
# print(c())
# print(id(c))
# print(c())

# from time import time

# def logged(when):
#     def log(f,*args,**kargs):
#         print('''
#            called:
#             function:%s
#             args:%r
#             kargs:%r
#               '''%(f,args,kargs))
    
#     def pre_logged(f):
#         def wrapped(*args,**kargs):
#             log(f,*args,**kargs)
#             return f(*args,**kargs)
#         return  wrapped
    
#     def post_logged(f):
#         now=time()
#         def wrapped(*args,**kargs):
#             log(f,*args,**kargs)
#             print('time delta:%s'%(time()-now))
#             return f(*args,**kargs)
#         return wrapped
    
#     return {'pre':pre_logged,'post':post_logged}[when]
 

# @logged('pre')
# def hello(name):
#     print('hello'+name)

# hello('ztj')

# j,k=1,2
# def procl():
#     j,k=3,4
#     print('j==%d and k==%d'%(j,k))
#     k=5

# def proc2():
#     j=6
#     procl()
#     print('j==%d and k==%d'%(j,k))

# k=7
# procl()
# print('j==%d and k==%d'%(j,k))
# j=8
# proc2()
# print('j==%d and k==%d'%(j,k))
# class roundfloat(object):
#     def __init__(self,val):
#         assert isinstance(val,float),"value must be a float"
#         self.value=round(val,2)
#     def __str__(self):
#         return '%.2f'%self.value

# class time60(object):
#     def __init__(self,hr,min) -> None:
#         self.hr=hr
#         self.min=min
#     def __str__(self) -> str:
#         return '%d:%d'%(self.hr,self.min)
# mon=time60(10,30)
# print(mon)
class aaa():
    pass
class wrapme(aaa):
    def __init__(self,obj) -> None:
        self._data=obj
    def get(self):
        return self._data
    def __str__(self) -> str:
        return str(self._data)
    __repr__=__str__
    # def __getattr__(self,stt):
    #     return getattr(self._data,stt)
    

wrap=wrapme(3.5+4.2j)
wra=wrap.get()
print(wra.real)
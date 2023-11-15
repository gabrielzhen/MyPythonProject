#!/usr/bin/env python
import _thread as theread
from time import sleep,ctime
loops=[4,2]
def loop(nloop,nsec,lock):
    print('start loop',nloop,'at:',ctime())
    sleep(nsec)
    print('end loop',nloop,'at:',ctime())
    lock.release()

def main():
    print('starting at:',ctime())
    locks=[]
    nloops=range(len(loops))
    for i in nloops:#allocate获取锁对象,acquire将锁上锁,上了锁的锁可以添加到列表中用于后面分配给子进程，让子进程进行锁的释放，主进程监控锁的状态。
        lock=theread.allocate_lock()
        lock.acquire()
        locks.append(lock)
        print(locks,type(locks))
    for i in nloops:#创建两个子线程，并在子线程里执行loop
        theread.start_new_thread(loop,(i,loops[i],locks[i]))
    for i in nloops:#主线程进行while监控 直到全部返回false退出循环
        while locks[i].locked():
            pass
    print('all done at:',ctime())

if __name__=='__main__':
    main()

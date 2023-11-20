from random import randint
from time import ctime
from queue import Queue
from mythread import mythread

def writeQ(queue):
    print('producing object for Q..')
    queue.put('xxx',1)
    print('size now',queue.qsize())

def readQ(queue):
    val=queue.get(1)
    print('consumed object from Q... size now',queue.qsize())

def writer(queue,loops):
    for i in range(loops):
        writeQ(queue)
        sleep(randint(1,3))

def read(queue,loops):
    for i in range(loops):
        readQ(queue)
        sleep(randint(2,5))

funcs=[writer,read]
nfuncs=range(len(funcs))


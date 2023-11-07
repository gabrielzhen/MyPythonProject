import os
print('create process %s'% os.getpid())
pid=os.fork()
if pid==0:
    print('i am children process %s' % pid)
else:
    print('i am farther process %s' % os.getppid())
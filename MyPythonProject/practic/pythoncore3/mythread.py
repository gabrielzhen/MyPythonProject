from collections.abc import Callable, Iterable, Mapping
import threading
from time import ctime

class mythread(threading.Thread):
    def __init__(self,func,args,name='') -> None:
        super().__init__(self)
        self.name=name
        self.func=func
        self.args=args

    def getResult(self):
        return self.res
    
    def run(self):
        print('starting',self.name,'at:',ctime())
        self.res=self.func(*self.args)
        print('finishing',self.name,'at:',ctime())
        

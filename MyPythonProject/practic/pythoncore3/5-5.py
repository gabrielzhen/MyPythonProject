from functools import partial as pto
from tkinter import Tk,Button,X
def bar(name):
    print('Hello %s' % name)

class Person(object):
    def __init__(self, name):
        print('Hello %s' % name)

def decorator_func():
    print('from decorator_func')
    return bar
deco_bar = decorator_func()
print('1')
deco_bar('deco_bar')
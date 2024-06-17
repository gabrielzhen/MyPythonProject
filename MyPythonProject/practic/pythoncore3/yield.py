import time
def sleep(seconds):
    starttime=time.time()
    while time.time()-starttime<seconds:
        yield

def task1():
    while True:
        print('task 1')
        yield from sleep(2)

def task2():
    while True:
        print('task 2')
        yield from sleep(5)

even_loop=[task1(),task2()]

while True:
    for task in even_loop:
        next(task)
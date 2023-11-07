class Student(object):
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def print_score(self):
        print('%s:%s'%(self.__name,self.__age))
bart=Student('ztj','22')
bart.print_score()
bart.__name='asdfsdf'
print(bart.__name)

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

def run_twice(animal):
    animal.run()
    animal.run()

class Tortoise(object):
    def run(self):
        print('Tortoise is running slowly...')
run_twice(Tortoise())
print(type(Tortoise()))
print(type(Animal()))
print(type(Dog()))
print(dir(bart))

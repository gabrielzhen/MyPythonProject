class dog():
    def __init__(self,name,age):
        self.names=name
        self.ages=age
    
    def sit(self):
        print('dog'+str(self.names)+' is siting')

    def roll(self):
        print('dog'+str(self.names)+' is rolling')

my_dog=dog('小新',6)
print(my_dog.names+str(my_dog.ages))
my_dog.sit()
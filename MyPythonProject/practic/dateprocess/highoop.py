###___slots___

####@property
class Student(object):
    #__slots__=('name','age','score')
    def set_age(self,age):
        self.age=age
    
    @property
    def score(self):
        return self.score
    @score.setter
    def score(self,score):
        self.score=score

s=Student()
s.scores=60
print(s.scores)


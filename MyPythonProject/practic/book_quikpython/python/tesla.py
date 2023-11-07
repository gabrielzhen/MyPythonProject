class car():
    def __init__(self,make,modle,year):
        self.make=make
        self.modle=modle
        self.year=year
    
    def get_description(self):
        long_name=self.make+self.modle+str(self.year)
        return long_name

class Battary():
    def __init__(self,battary_size=80):
        self.battary_size=battary_size

    def des_battary(self):
        print(self.battary_size)

class elecar(car):
    def __init__(self,make,modle,year):
        super().__init__(make,modle,year)
        self.battary=Battary()
    


tesla=elecar('tesla','model s','2022')
tesla.battary.des_battary()

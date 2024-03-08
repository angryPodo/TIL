class human():
    populality = 0
    def __init__(self,name,age,sex):
        self.sex = sex
        self.name = name
        self.age = age
        human.populality+=1
        
class sport_player(human):
    def __init__(self, name2, age2, sex2,speed,power):
        super().__init__(name2, age2, sex2)
        self.speed = speed
        self.power = power
    def move(self):
        self.speed+=10

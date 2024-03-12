class human():
    populality = 0
    def __init__(self,name,age,sex):
        self.sex = sex
        self.name = name
        self.age = age
        human.populality+=1
        
class sport_player(human):
    def __init__(self, name, age, gender,speed,power):
        super().__init__(name, age, gender)
        self.speed = speed
        self.power = power
    def move(self):
        self.speed+=10

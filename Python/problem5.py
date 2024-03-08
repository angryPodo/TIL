class Person():
    species = "Homosapiens"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print("Hello, my name is",self.name,"and I'm",self.age,"years olds.")
    def celebrate_birthday(self):
        self.age = self.age + 1
        print("Happy Birthday!",self.name,"is now",self.age,"years old.")

class SocialPerson(Person):
    def __init__(self, name, age, ad, hobby):
        super().__init__(name, age)
        self.adress = ad
        self.hobby = hobby
    def greet(self):
        super().greet()
        print("I am from",self.adress,"and I like",self.hobby,"so much.")

person1 = SocialPerson("Alice", 25, "Seoul" , " soccer" )
person2 = SocialPerson("Bob", 30, "Yongin" , "computer game")

person1.greet()
person2.greet()
person1.celebrate_birthday() # 출력: Happy Birthday! Alice is now 26 years old.
person2.celebrate_birthday() # 출력: Happy Birthday! Bob is now 31 years old.
person1.greet() # 출력: Hello, my name is Alice and I’m 26 years old.
person2.greet() # 출력: Hello, my name is Bob and I’m 31 years old.
print(Person.species)
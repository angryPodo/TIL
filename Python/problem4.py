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

person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# 메서드 호출

person1.greet() # 출력: Hello, my name is Alice and I'm 25 years old.

person2.greet() # 출력: Hello, my name is Bob and I'm 30 years old.

# 다른 메서드 호출

person1.celebrate_birthday() # 출력: Happy Birthday! Alice is now 26 years old.

person2.celebrate_birthday() # 출력: Happy Birthday! Bob is now 31 years old.

person1.greet() # 출력: Hello, my name is Alice and I’m 26 years old.

person2.greet() # 출력: Hello, my name is Bob and I’m 31 years old.
print(Person.species) # 출력: Homosapiens

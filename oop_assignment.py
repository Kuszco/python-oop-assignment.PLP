class Person:
    def __init__(self, name, age, gender):
        self.name=name
        self.age=age
        self.gender=gender
    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I'm a {self.gender}")

person1= Person ("Solomon", 22, "male")
person1.introduce()
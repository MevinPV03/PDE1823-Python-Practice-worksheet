class Student:
    def __init__(self, name, age, programme):     #names etc are attributes
        self.name = name                          #self shows that name is for that specific class
        self.age = age
        self.programme = programme

    def introduce(self):                           #introduce() is a method
        print(f" My name is {self.name}.")
        print(f"I study {self.programme}.")

student1= Student("Aisha", 18, "Robotics")     #student1 is an object
student1.introduce()
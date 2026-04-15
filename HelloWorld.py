# Inheriance
# super class

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name}, the {self.breed} is speaking")

# sub-class
class Dog(Animal):
    def __init__(self, name, age, breed, color=None):
        super().__init__(name, age)
        self.breed = breed

dog = Dog("Jack", 7, "German Shepherd")
dog.speak()

class Mammal:
    
    def walk(self):
        print(f"walk")


class Dog(Mammal):
    def bark(self):
        print(f"bark")


class Cat(Mammal):
    def meow(self):
        print(f"meow")


cat1 = Cat()
cat1.meow()


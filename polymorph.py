class Human():
    def __init__(self, name, id):
        self.name
        self.id

    def move(self):
        return f"{self.name} is moving"

class Man(Human):
    def move(self):
        return f"{self.name} is walking"

class Woman(Human):
    def move(self):
        return f"{self.name} is flying"

class ManWoman(Human):
    def move(self):
        return f"{self.name} is crawling"

 
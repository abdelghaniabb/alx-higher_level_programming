"""Real World Objects : Attributes & Capabilites
Dog Attribute (Fields / Variables) : Height, Weight, Favorite Food
Dog Capabilites (Methods / Functions) : Run, Walk, Eat"""
class Dog:
    def __init__(self, name="",hieght=0, weight=0):
        self.name = name
        self.hieght = hieght
        self.weight = weight

    def run(self):
        print("{} the dog runs".format(self.name)) 

    def eat(self):
        print("{} the dog eats".format(self.name))

    def bark(self):
        print("{} the dog braks".format(self.name))

def main():
    spot = Dog("Spot", 66, 25)
    spot.bark()
    
    bowser = Dog()
    bowser.bark()


main()
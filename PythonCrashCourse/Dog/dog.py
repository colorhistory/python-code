class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def rollOver(self):
        print(self.name.title() + " rolled over")


myDog = Dog("white cat", 4)
print(myDog.name.title())
print(myDog.age)

myDog.sit()
myDog.rollOver()

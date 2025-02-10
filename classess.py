class Animal:
    def __int__(self, name):
        self.name = name

    def eat(self):
        print("Eating........")
        def breathe(self):
            print("Breathing....")

class Dog(Animal):
    def sound(self):
        print("Barking...")

class Cat(Animal):
    def sound(self):
        print("Meow...")

dog1 = Dog("Jack")
dog1.eat()
dog1.sound()

cat1 = Cat("cat")
cat1.eat()
cat1.sound()
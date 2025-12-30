from abc import ABC, abstractmethod

# Base class with no implementation of methods
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass # no implementation

# derived classes with implementation
class Lion(Animal):
    def make_sound(self):
        print("Roar")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

class Cow(Animal):
    def make_sound(self):
        print("Moo")

lion = Lion()
lion.make_sound() # Roar!

cow = Cow()
cow.make_sound() # Moo!

cat = Cat()
cat.make_sound() # Meow!
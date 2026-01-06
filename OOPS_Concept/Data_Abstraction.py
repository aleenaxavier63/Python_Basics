from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    def eat(self):
        print("Animal eats")

class Cat(Animal):
    def sound(self):
        print("cat makes sound")

c1=Cat()
c1.sound()
c1.eat()

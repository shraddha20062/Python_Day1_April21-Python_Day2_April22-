
from abc import ABC,abstractmethod
class Animal(ABC): #abstract class
    @abstractmethod
    def eat(self): #abstract method
        pass

class Tiger(Animal):
    def eat(self):
        print("tiger eat non veg food")
class Cow(Animal):
    def eat(self):
        print("cow eat veg")

t1=Tiger()
t1.eat()
c1=Cow()
c1.eat()
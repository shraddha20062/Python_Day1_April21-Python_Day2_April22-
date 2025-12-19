#abstract class-It is class that contain one or more abstract method.method is declared but contains no implementation.
#abstarct classes cannot be initiated and required to provide implementation for abstract method.
#sub class of abstract class in python are not required implement because  abstract method in parent class.


#ABC is predefined abstract class

from abc import ABC,abstractmethod
class A(ABC): #Abstract class
    @abstractmethod
    def display(self): #abstarct method
        none

class B(A):
    def display(self):
        print("this is display method")
#obja=A()
#obja.display()
obj=B()
obj.display()

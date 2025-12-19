
#inheritance-aquaring all attribute

class A: #Parent class or superclass or main class
    def m1(self):
        print("this is method 1 from Class A")
class B(A): #child class or subclass or derived class
    def m2(self):
        print("this is method 2 from class B")

a1=A()
a1.m1()

b1=B()
b1.m2()
b1.m1()

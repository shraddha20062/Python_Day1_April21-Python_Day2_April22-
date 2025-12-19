#there are 3 types of variable

#1.global variable--means kept outside all methods. need to declare only time
#2.local variable---which access within method
#3. class variable--- any variable belong to class

url="http://www.facebook.com" #global variable
class myclass:
    userName,password="vivek","vivek123" #class variable boz its created in class
    def screenshots(self,path): #path is local variable
        print(url) #global variable can access directly anywhere in class
        print("screenshots is taken---->",path)
        print(self.userName) #to access class level variable use self keyword
        print(self.password)

m1=myclass()
m1.screenshots("d\:screenshots.jpg")
print(url)
#print(path) #local variable cannot access outside method

#Example 4

class newClass:
    def __init__(self):
        print("this is constructor")
    def m1(self):
        print("this is method1")

n1=newClass() # constructor will get call automatically when we created obj of class
#its use for initialization purpose
n1.m1()
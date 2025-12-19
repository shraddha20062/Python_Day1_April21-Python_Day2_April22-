

def doLogin(): #step 1 create or define function
    print(" step 1 open browser and type website url")
    print(" step 2 enter vald username-demo")
    print(" step 3 enter valid password-demo")
    print(" step 4 click on login in")
    print(" step 5 close the function")

def register(username, createpwd,confirmpwd):
    #username,createpwd,confirmpwd input parameter
    print(" username-------->",username)
    print(" create password is ---->",createpwd)
    print("confirm password is ---->",confirmpwd)
#example 3
def cal(a,b):
    return(a+b)
def verifytext():
    text="tina"
    return text

doLogin() #calling the function
register("shraddha","test","test")
register("rina","test2","test2")
Sumresult=cal(100,200)
print(Sumresult)

firstName=verifytext()
print("firstname is--------->",firstName)
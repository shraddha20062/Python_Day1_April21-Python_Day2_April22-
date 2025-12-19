# WAP advise the user what to wear based on temp
# Hot :- above 30, warm>-20 to 30, cool:- 10to 20, cold:- below 10

temp = int(input("enter temp--->"))
print(" temp is--->" , temp)

#print(type())
if temp>30: # first condition
    print("Its hot.wear light and breathable clothing")
elif 20<=temp<=30: #second condition
    print( "its warm. wear casual clothing")
elif 10<=temp<=20:
    print("its cool. wear light jacket OR Sweater")
else:
    print("Its cold. wear warm clothing and layers")


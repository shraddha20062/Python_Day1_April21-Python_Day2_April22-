# example 1 create Tuple
#store multiple values. values are immutable or fix. round() bracket to store all values.

mytuple=("apple","banana","cherry")
print(mytuple)
mytuple2=() #empty tuple
print(mytuple2)
# example access tuple values/items
print(mytuple[1]) #access 1st index value. index start with 0
print(mytuple[-1]) # its takes ndex from right to left if index is given negative
#example 3 range of index. Tuple slicing to fetch specific values.
mytuple=("apple","banana","cherry","mango","kiwi","melon","orange")
print(mytuple[2:5])
print(mytuple[-4:-1]) #(-7,-6,-5,-4,-3,-2,-1)
print(mytuple[:])
print(mytuple[:4])
print(mytuple[4:])

#example 4 change items from tuple
#by default it is not possible tuple dont allow to change values
mytuple=("apple","banana","cherry")
#covert tuple value to list
mylist=list(mytuple)
mylist[0]="orange"
#convert list to tuple
mytuple=tuple(mylist)
print(mylist)
#example 5 reading tuple items from Loop
mytuple=("apple","banana","cherry",1,2)
for i in mytuple:
    print(i)
#example 6 check items exit in tuple
mytuple=("apple","banana","cherry",1,2)
if "cherry" in mytuple:
    print("yes, cherry is present")
else:
    print("no, cherry is not present")
#example 7 tuple length- counting item in tuple
mytuple=("apple","banana","cherry",1,2)
print(len(mytuple))

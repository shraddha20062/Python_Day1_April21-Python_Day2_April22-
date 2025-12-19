

emp1="shraddha"
emp2="tejaswini"
mylist1=[10,33,55,77,88,"shina"]
print(mylist1)
mylist2=["apple","banana","mango"]
print(mylist2)
mylist3=list()
print(mylist3)
#example 2 access items from list
mylist2=["apple","banana","mango"]
print(mylist2[2]) # index start with 0
#example 3 range of index using slicing
mylist2=["apple","banana","mango","kiwi","melon","cherry","orange"]
print(mylist2[2:5])
print(mylist2[:3]) # start index not mention then start with 0th index
print(mylist2[4:]) # if end index not mention then it goes till last value
print(mylist2[:]) # print all values start and end is not mention
#example 4 Read the list items using loop
mylist4=["apple","banana","mango","kiwi","melon","cherry","orange"]
for i in mylist4:
    print(i)
#example 5 verify if the items or values exist in list
mylist4=["apple","banana","mango","kiwi","melon","cherry","orange"]
if "mango" in mylist4:
    print("yes, mango is there in basket. its my fav fruit")
else:
    print("no i will purchase")
#example 6 list length counting number of items on list
mylist4=["apple","banana","mango","kiwi","melon","cherry","orange"]
print(len(mylist4)) #use function len to count total values from list
mylist4.append("musk melon")#new value will be added end of list
print(mylist4)
mylist4.insert(10,"car")
mylist4.insert(11,"banana")
print("insert function outputs:-",mylist4)
print(len(mylist4))#9
# example7 remove item from list use pop method
mylist4=["apple","banana","mango","kiwi","melon","cherry","orange"]
mylist4.pop(3) #pop method accept index which value want to remove
print(mylist4)
#example 8 using del keyword we can also delete value
mylist4=["apple","banana","mango","kiwi","melon","cherry","orange"]
del mylist4[5]# here del command remove single item based on index
print(mylist4)
# example10 clear()
mylist4.clear() #clear "ALL" items from memory but list is there
print(mylist4)
# set is a collection which is unordered or unindexed.in python set are written with {} bracket.
# set is muttable
#example 1 Create Set
myset={"apple","cherry","banana"}
print(myset)

#example 2 Accessing vallues from set
myset={"apple","cherry","banana"}
for i in myset:
    print(i)
#example 3 verify values in set
print("banana" in myset) #true
print("mango" in myset) #false

#example 4 adding values in set
myset={"apple","cherry","banana"}
myset.add("mango") # add method will add value but in random
print(myset)
#how to add multiple vales in set using update()
myset.update(["grapes","kiwi","strawberry"])
print(myset)

#Example 5 Find element in set
#myset={"apple","cherry","banana"}
print(len(myset))

#example 6 how to remove values from set use remove(),discard()

myset.remove("kiwi")
#myset.remove("test) throws key error if value is not present
print(myset)
print(len(myset))
myset.discard("grapes")
myset.discard("test") # if value not present it doesnt throw error
print(myset)
print(len(myset))


#WAP to print values from 1 to 10
# range (start point,end point[excluded.last value -1],increment--increase value by 1
# WAP to print the table of 5 value
table=int(input("please enter your valid number to create table"))
print("table of --->",table)
for i in range (1,11,1):

#print("values in increment order",i)
      print(table * i)
print("-------------------------------")
#wap print values from 10 to 1
for j in range (10,0,-1):
    print("values decrement order is---->",j)
#WAP print even no from 1 to 100

for i in range(1,101,1):
#% mod operator divide 2 no and return reminder
    if i % 2==0:
        print(i)
    else:
        print(i)

#wap to print odd 1 to 100
for i in range (1,101,1):
    if i % 2==1:
        print(i)


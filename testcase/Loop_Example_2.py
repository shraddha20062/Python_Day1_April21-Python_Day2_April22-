#WAP to print table of range 1 to 5
# nested for loop loop within loop
for i in range(1,6,1): #outer for loop 1 to 5
    print("----------------")
    print("table of ----->",i)
    for j in range(1,11,1): # inner for loop table creation
       print(i*j)

# i=1, j=1
# i=1, j=2
# i=1, j=3......j=10
#i=2,
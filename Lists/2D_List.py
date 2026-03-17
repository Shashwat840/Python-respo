data=[[1,2,3],[4,5,6],[7,8,9]]
# Printing of 2d list via range loop
for i in range(0,len(data)):
    for j in range(0,len(data[i])):
        print(data[i][j] , end=" ")
    print()
print("----------------------")

#Printing 2D list via for each loop
#Proper Pythonic way to do it
for i in data:
    for j in i:
        print(j,end=" ")
    print()

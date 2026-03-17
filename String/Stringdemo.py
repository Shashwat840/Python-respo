#blank string

x=""
print(x)
print("Type of :- ",type(x))
name = "India is my Country"

# Finding length of string

length = len(name)
print("Length = " ,length)

# for i in range(0,5):
#     print(name[i])

# for i in range(0,length):
#     print(name[i])

# for i in range(0,len(name)):
#     print(i,"-",name[i])


#for each loop

#by default it will start from 0 end goto end of string
for i in name:
    print(i,end="")
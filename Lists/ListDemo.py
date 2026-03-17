li = [1,2,3,'Hi','Shashwat']
# print(type(li))
# print(li)

# for i in li:
#     print(i)
# li.append(False)
# print(li)


# append==> Adds element to last place
# li.append(123)
# print(li)

#insert==> Insert element at desired index
# li.insert(2,"Radhe")
# print(li)
# li2= ["Hello","kemCho"]

#extend==> Add the argument string to the mentioned string 
# li.extend(li2)
# print(li)

data=[]

while "exit":
    name = input("Enter your name:- ")
    if(name == "exit"):
        break
    else:
        data.append(name)
        print(data)
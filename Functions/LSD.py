def listFun():
    users = ["Ram","Raj","Ramesh"]
    users.extend(["Krishna","Suresh","Ramlal"])
    return users
print(listFun())

def dictFun():
    d = {1:"Ajay",2:"Parth",3:"Shrey"}
    d.update({3:"priya",4:"neha",1:"vijay"})
    return d
print(dictFun())

def setFun():
    data1 = {"ram","seeta","lakshman","kush","luv","krishna"}
    data2 = {"ram","arjunn","bhim","sahdeve","krishna","draupadi"}
    data3 = data1 & data2
    return data3

print(setFun())
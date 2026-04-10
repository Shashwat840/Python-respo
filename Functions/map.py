# sales = [100,200,500,1000]
# users = ["Shashwat","Shrey","Raj","Jaimin"]
# discount = map(lambda x:x*1.3,sales)
# print(list(discount))
# #Filter

# userwithLen = list(filter(lambda x:len(x)>4,users))
# print(userwithLen)
# Make a new list using filter and map in which store the values having last letter "a" and convert those values in uppercase
names =["amit","neha","smruti","priya","ajna","amita","mayavati","sushila","radha","jay"]
# namewitha = list(filter (lambda x:x[-1]=="a",names))
# uppercase = list(map(lambda x: x.upper(), namewitha))
# print(uppercase)

name2 = list(map(lambda x:x.upper(),filter(lambda x:"i" in x, names)))
print(name2)
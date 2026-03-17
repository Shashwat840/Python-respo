data1 = {"ram","seeta","lakshman","kush","luv","krishna"}
data2 = {"ram","arjunn","bhim","sahdeve","krishna","draupadi"}
# union --> combines both the elements
x= data1.union(data2)
#x= data1 | data2
print(x)
# intersection --> common elements of both sets
y = data1.intersection(data2)
#y = data1 & data2
print(y)
#symmetric_diffrence --> union of both set - intersection of both set
z = data1.symmetric_difference(data2)
print(z)

c= data1.difference(data2)
#c = data1 - data2
print(c) 

a = data1.issubset(data2)
print(a)
#issuperset--> Excatly all the elements in data1 are in data2
b=data1.issuperset(data2)
print(b)
data = {"ram","krishna","arjun"}
print(data)
removedElm = data.pop()
print(removedElm)
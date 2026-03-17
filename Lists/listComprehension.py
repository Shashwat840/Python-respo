users = ["ram","shyam","amit","sumit","jaya","divya"]


#uppersUser=[]
#This list will convert all names to upper case
upperUser =[]
for i in users:
    upperUser.append(i.upper())
print(upperUser) 

#comprehension version...
#Syntax:- [i function/operation for i in iterable]
upperUser1 = [i.upper() for i in users]
#[return[append]i for i in users]
print(upperUser1)

users = ["ram","shyam","amit","sumit","jaya","divya"]
#This list will contain first letter of each name
usersInitial = []
for i in users:
    usersInitial.append(i[0])

print(usersInitial)    

#comprehension version...
usersInitial1 = [i[0] for i in users]
print(usersInitial1)


#numric
sales = [100,200,300,400,500,600,700] 
#Adding 10 to each value in sales
#10...
#sales1 = [110,210]
sales1 =[]

for i in sales:
    sales1.append(i+10)

print(sales1)   

#comprehension version...
sales2 =[i+10 for i in sales] 
print(sales2)

#%10% profit

profitPercent = [int(i*1.1) for i in sales]
print(profitPercent)
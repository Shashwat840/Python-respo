x = lambda x: "Even" if x%2==0 else "Odd"
print(x(201))

x2= lambda name: "Pallindrome" if name == name[::-1] else "Not pallindrome"
print(x2("shashwat"))

x3 = lambda no1,no2 : no1 if no1>no2 else no2
print(x3(10,20))
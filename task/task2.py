#Find bigger number and store it in max
min=None
max=None
no1=float(input("Enter 1st Number:- "))
no2=float(input("Enter 2nd Number:- "))
if(no1>no2):
    print(f"{no1} is the max value")
    max=no1
    min=no2
else:
    print(f"{no2} is max")
    max=no2
    min=no1
print(f"Max value is:- {max}")
print(f"Min value is:- {min}")
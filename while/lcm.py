no1= int(input("enter number:- "))
no2= int(input("enter number:- "))
max=0
if (no1>no2):
    max=no1
else:
    max=no2

while True:
    if(max%no1==0 and max%no2==0):
        lcm=max
        break
    max+=1
print(max)
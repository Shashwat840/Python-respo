no=int(input("Enter Your number:- "))
temp=no 
sum=0
count=0
rem=0
while(temp>0):
    rem= no//10
    count+=1

print(count)

while(temp!=0):
    rem= temp%10
    sum = sum +(rem**count)
    temp=temp//10

if(temp==sum):
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")

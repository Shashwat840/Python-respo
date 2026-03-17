a=0
b=0
c=0
count=0
dig=0
dig2=0
dig3=0
dig4=0
bal=int(input("Enter Amount:- "))
if(bal>=500):
    a= bal-500
    count+=1
    print(f"500*{count}")
    if(bal>=200):
        b=bal-200
        dig+=1
        print(f"200*{dig}")
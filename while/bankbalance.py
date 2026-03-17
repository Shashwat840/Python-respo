count=0
while(3):
    balance=int(input("Enter bank balance:- "))
    if(balance>=10000):
        print("account opened successfully")
        break
    else:
        print("Enter valid Balance")
        count+=1
        if(count==3):
            break
        

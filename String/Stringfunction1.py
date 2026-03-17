name= input("Enter your name in small letter:- ")
upperName= ""
#hello
#h--->H
for i in name :
    if(ord(i)>=65 and ord(i)<=90):
        upperName= upperName + chr(ord(i)-32)
    
    else:
        upperName = upperName + i

print(upperName)
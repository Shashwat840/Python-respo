name = "Shashwat#14"
digit = 0
alphabet=0
specialchar=0

for i in name:
    if(i.isnumeric()):
        digit+=1
    elif(i.isalpha()):
        alphabet+=1
    else:
        specialchar+=1
print(digit)
print(alphabet)
print(specialchar)
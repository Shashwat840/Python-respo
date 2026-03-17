colors = ['RED' , 'ORANGE' , 'BLACK','YELLOW' , 'BLACK' , 'VIOLET',"YELLOW" , "YELLOW"]
uniqueList = []
new=[]
for i in colors:
    if i not in uniqueList:
        uniqueList.append(i)
    else:
        new.append(i)

print(new)
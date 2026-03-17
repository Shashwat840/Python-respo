name= "Java"
index=None
char = input("Enter charater you want to search:- ")
for i in range(0,len(name)):
    if(name[i]== char):
        index = i
        break
print(f"Your {char} is loacated at {index} index ")
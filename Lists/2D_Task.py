players =[["Virat",100,121,89],["Rohit",100,67,56]]
sum = 0
#print both player name
#print virat score 
#Print virat score total
#print rohit score total
#print total score by both player
print("Name of both players")
for i in players:
    for j in i:
        if type(j) == str:
            print(j)
    print()
print("Virat score")
for i in players:
    for j in i:
        if i[0] == "Virat":
            print(j)

for i in players:
    if i[0] == "Virat":
        sum = sum + i[1] + i[2] + i[3]

print(sum)
sum1 = 0
for i in players:
    if i[0] == "Rohit":
        sum1 = sum1 + i[1] + i[2] + i[3] 
print(sum1)
print("Total score of both player")
print(sum + sum1)

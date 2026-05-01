data = {"rohit":[100,20,121],"Virat":[90,98,78],"Kl":[151,89,7]}

score = 0
for player in data:
    print("Player Name :- ",player)
    for i in range(len(data[player])):
        file = open(f"{player}.txt","a")
        file.write(f"Match {i+1}:- {data[player][i]}\n")
        print(f"Match {i+1}:- ",data[player][i])
        file.close()
        score = score + data[player][i]

print("Total:- ",score)
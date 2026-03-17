data = {"Virat":[123,78,81],"Rohit":[142,67,21],"Hardik":[52,67]}
print(data)
sum=0
totalScore =0
for i,j in data.items():
    print(f"{i}")
    for r in j:
        sum+=r
        print(r)
    print("total =",sum)
    totalScore+=sum
    sum=0
print("total score ==",totalScore)
max = 0
for i,j in data.items():
    sum = 0
    for r in j:
        sum += r
    print(f"Total runs for {i}: {sum}")
    if sum > max:
        max = sum
print(f"Maximum total runs: {max}")




        

data = {"Virat":[123,78,81],"rohit":[142,67,21]}
print(data.keys())
print(data.values())
print(data.get("Virat"))
data.get("Virat")[2] = 100
# y = data.get("Virat")
# y[1]=90
print(data)
data.update({"Hardik":[52,67]})
print(data)
for i,j in data.items():
    print(f"{i}")
    for r in j:
        print(r)
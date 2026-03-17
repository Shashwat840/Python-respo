data = {"Guj":"Gandhinagr","Mah":"Mumbai","Tamilnadu":"Chennai","Guj":"Ahm","Punjab":"Chandigadh","Hariyana":"Chandigadh"}
print(data)
print(data["Guj"]) #if key is not present it will throw exception
print(data.get("Guj")) #""  ""  None

#keys...
k = data.keys() #list
print(k)
v = data.values() #values
print(v)

kv = data.items()
print(kv)

for i,j in data.items(): #2d array [(k,v),(k,v)]
    print(f"{i} - {j}")

# for i in data:
#print(i)
#pop value at particular index
data = {101:"raj",102:"parth",103:"jay"}
if 101 in data:
    removedData = data.pop(101)
    print(removedData)
else:
    print("Key not found")
print(data)
#pop removes particular key value pair
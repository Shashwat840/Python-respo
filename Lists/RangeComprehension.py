data = []

for i in range(1,6):
    data.append(i)
print(data)

#By comprehension meathod
data2 = [i**2 for i in range(1,6)]
print(data2)

data3 = [i for i in range(1,6,2)]
# [1,3,5]
print(data3)
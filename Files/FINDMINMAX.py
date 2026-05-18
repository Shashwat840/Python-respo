# Find min max using functions 
# data = (1,2,3,4,5,-1,-20)
# minimum = min(data,key= lambda x:abs(x))
# maximum = max(data,key= lambda x:abs(x))
# print("Minimum is ",minimum)
# print("Maximum is ",maximum)

# name = ["Raj","Parth","Amitab"]

# minnimum = min(name,key = len)
# maximum = max(name,key=len)

# print("Minimum is ",minnimum)
# print("Max is:- ",maximum)

# student = [("sam",18),("raj",20),("parth",15)]

# mini = min(student,key = lambda x:x[1])
# print(list(mini))

# nums = [-5,2,-1,7,1,6]
# #Find number near to x = 0
# minimum = min(nums,key= lambda x:abs(x))
# print("Minimum is:- ",minimum)

# str = ["ABC","ACBD","PQRSTU","PQRSTUV"]
# maximum = max(str, key=lambda x: len(x) if len(x) % 2 == 0 else 0)
# print("Maximum Length str is:- ",maximum)
# #Find sum of list named nums
# Find_nums = sum(i for i in nums if i % 2 == 0)
# print(Find_nums)

num = [1,2,3,4]
# sum = sum(i**2 for i in num)
# print(sum)
# data = "Shashwat"
# s = sum(i in "aeiou" for i in data)
# print(s)

num = 1234
# Find even digit sum
dig_sum = sum(int(d) for d in str(num) if int(d) % 2 == 0)
print(dig_sum)
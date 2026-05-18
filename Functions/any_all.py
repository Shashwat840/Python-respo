# marks = [27,19,15,18]
# flag = all(m>15 for m in marks)

# print(flag)

# flag1 = any(m>25 for m in marks)

# print(flag1)

students = {"amit":33,"summit":24,"raj":23,"ajay":25,"sujay":23}

# flag = all(mrks[1] > 20 for mrks in students.items())
# print(flag)

# bonus = any(mrks[1] > 25 for mrks in students.items())
# print(bonus)

# Sorting of list via sort fun
sorted_list = sorted(students,key= lambda x:x[1],reverse=True)
print(sorted_list)

sort = sorted(students.items(),key= lambda x:x[1],reverse=True)
print(dict(sort))
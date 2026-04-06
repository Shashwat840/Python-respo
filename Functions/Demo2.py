# #check type of data if string then yes else no
# def data(**kwargs):
#     print(kwargs)
# data(name="Shashwat",hobbies="Volleyball",city="Ahm",country="India")
# for i in data(name="Shashwat",hobbies="Volleyball",city="Ahm",country="India"):
#     print(i)
#     if type(i) == str:
#         print("Yes")
#     else:
#         print("No")
data1 = {"ram","seeta","lakshman","kush","luv","krishna"}
data2 = {"ram","arjunn","bhim","sahdeve","krishna","draupadi"}
print(data1)
print(data2)
data1.intersection_update(data2)
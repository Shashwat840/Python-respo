#Create a school data in which school has 3 std 10,11,12 and each has 5 students

school = {10:{"Ram","Shyam","Krishna","Dhurandhar","Lakhan"},
          11:{"Mohanpreet","Krishna","Rahul","Sam","Jacks"},
          12:{"Rohit","Suresh","Krishna","Vikram","Ravi"}}
std10 = school[10]
std11 = school[11]
std12 = school[12]

#1) Find common name from above students
common = std10.intersection(std11).intersection(std12)
print(common)

#2) give all students name
all = std10 | std11 | std12
print(all)

#3) give only unique students name
unique = std10.symmetric_difference(std11) | std10.symmetric_difference(std12)
print(unique)
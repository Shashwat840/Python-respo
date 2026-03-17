#we have 7 days sales data 3 time data morning,ev,noon
#find which day[monday,tue...] has heighest sale

sales = {"Monday":{10000,2500,4561},
         "Tuesday":{2000,8500,8888},
         "Wednesday":{8888,6969,5555},
         "Thrusday":{7979,9999,8789},
         "Friday":{7410,8520,9663},
         "Saturday":{7894,5612,6123},
         "Sunday":{9510,7530,8520}}
maxSales = 0
day = ""
for i,j in sales.items():
    total = sum(j)
    if total > maxSales:
        maxSales = total
        day = i
print(f"{day}---{maxSales}")
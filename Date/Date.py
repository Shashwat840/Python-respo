import datetime
import time 
import calendar
from datetime import date
today = date.today()
# print(today)
# print(type(today))

# #Access year month day 
# print(today.day)
# print(today.month)
# print(today.year)
# d --> day 
# m --> Months in digs 
#b --> Months in alphabets 
#M --> Minutes
#p --> Gives AM / PM
print(today.strftime("%d-%m-%Y"))
print(today.strftime("%b"))
print(today.strftime("%B"))
print(today.strftime("%I"))
print(today.strftime("%H"))
print(today.strftime("%b"))
print(today.strftime("%p"))
print(today.strftime("%S"))


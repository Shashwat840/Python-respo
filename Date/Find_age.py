#Find the month age and days diffrence between current date and date of birth
import datetime
import calendar
import time
from datetime import date
#find bday 
#today---->bd---->
#12 month ----> bday
#find birthday remaining month and days

from datetime import date

#input bdate
byear = date(2007,6,30)

#tdate
today = date.today()
years = today.year - byear.year
months = today.month - byear.month
days = today.day - byear.day

if days < 0:
    months -= 1
    days += 30

if months < 0:
    years -= 1
    months += 12

print("Age =", years, "Years", months, "Months", days, "Days")
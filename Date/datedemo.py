from datetime import time as tm
from datetime import datetime
#hrs,mins,secs
t=tm(14,30,35)
print(t)
print(t.hour)
print(t.minute)
print(t.second)

# timestamp
now = datetime.now()
print(now)

# beggining of the calander 1 jan 1970 --> imp
dt = datetime.fromtimestamp(0) #1ms pass
print(dt)

dtnow = datetime.fromtimestamp(now.timestamp())
print(dtnow)

#ctime
print(now.ctime())
#isofomrmate
print(now.isoformat())

#replace -->  Used to replace or to manupulate the datetime 
new_date = now.replace(year=2032,month=1)
print(new_date)
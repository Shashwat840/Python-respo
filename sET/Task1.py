mumbai ={"raj","parth","amit","sumit"}
pune = {"jay","amit","kunal","neha"}
goa = {"rajvi","priya","amit","neha","krishna","raj"}

 
#find user who have attended all 3 events
#find user who is present in mumbai and goa
#find user who is present in pune and goa
#find user who is present in mumbai and goa but not in pune
#find user who is not presnt goa but mummbai and pune both

all3Events = mumbai&pune&goa
print(all3Events)

mumGoa = mumbai&goa
print(mumGoa)

puGoa = pune&goa
print(puGoa)

a= (mumbai&goa)-pune
print(a)

b = (mumbai&pune)-goa
print(b) 
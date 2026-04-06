def getUserData(x,**kwargs):
    print("Kwargs" , kwargs)
    print("x" ,x)
getUserData(100,name="Shashwat",age=19,Marks=99)
def getData(*args,**kwargs):
    print("args ",args)
    print("kwargs",kwargs)

getData(10,20,30,40,name="Shashwat",age=19,Marks=99)
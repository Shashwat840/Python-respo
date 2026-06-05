class Demo:
    # This varible can be accessed by both obj and class varible
    x = 100 # it is know as class level varible or static variable
    
    #self:- by default when we make an obj it's address is passed thus self is used to handle that address 
    def fun(self):
        print("Function is called")
        self.no = 200 # Instance varible It is a varible that is called everywhere by both class and object
        no1 = 20 # it is local varible which is only called by the fun not by class or obj
    def testFun(self):
        print("No :- ",self.no)

d = Demo() #--> it is the meathod to create an object 
d.fun() # --> it will pass the parameter like d.fun(d) thus self is used to take value of d
print(d.x)
print(d.no)
d.testFun()
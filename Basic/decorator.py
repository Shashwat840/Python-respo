def checkGrade(func):
    def inner(name,**kwargs):
        if "maths" in kwargs and "sci" in kwargs and "phy" in kwargs:
            if kwargs["maths"] > 0 and kwargs["sci"] > 0 and kwargs["phy"]>0:
                total = (kwargs["maths"] + kwargs["phy"] + kwargs["sci"])/3
                print("The grade of student:- ",total)
            else:
                print("Enter marks of the subjects")
        else:
            print("Your grade is C")
    return inner

@checkGrade
def grade(name,**kwargs):
    pass

grade("Shrey",maths = 90,sci = 69,phy = 80)
grade("Jaimin")
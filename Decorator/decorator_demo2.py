def checkValidity(func):
    def inner(name, **kwargs):
        if "age" in kwargs and "course" in kwargs:
            if kwargs["age"] >= 18:
                func(name, **kwargs)
            else:
                print("Your age is not valid for admission")
        else:
            print("Please provide both age and course details for admission")   
    return inner

@checkValidity
def admission(name,**kwargs):
    print("Your addimission is accepted...")


admission("raj",age="19",course="IT") #valid
admission("parth",age="16",course="CS") #not valid age <18
admission("jay",course="IT") #not valid age is not present
admission("amit") #not valid both age and course not present
admission("kunal",age="22") #not valid course not present
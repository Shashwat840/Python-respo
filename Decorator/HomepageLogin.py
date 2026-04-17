def login_details(func):
    def inner(role,*args):
        if role in args:
            func(role,args)
        else:
            print("Invalid user indentified")
    return inner
role = input("Enter your role: ")

@login_details
def pageDetalis(role,*args):
    print("Page access accepted",role)

pageDetalis(role,"User","Admin","Manager")

@login_details
def cart_access(role,*args):
    print("Cart access provided to ",role)

cart_access(role , "User","Admin")
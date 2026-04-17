def login_req(func):
    def inner(role):
        if(role == "ADMIN" or role == 'Admin'):
            func(role)
        else:
            print("Unauthorised person found")
    return inner

@login_req
def data_of_files(role):
    print("Accessing files...",role)

role = input("Enter your role:- ")
data_of_files(role)
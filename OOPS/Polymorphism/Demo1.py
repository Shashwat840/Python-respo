from multipledispatch import dispatch
class Bank:

    def __init__(self):
        print("Default constructor called")
    
    @dispatch(int)
    def BankDeposit(self,a):
        print("Value of single arguments:- ",a)

    @dispatch(int,int)
    def BankDeposit(self,a,b):
        print("Value of two argument is:- ",a,b)

b = Bank
b.BankDeposit(10)
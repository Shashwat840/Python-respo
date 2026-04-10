def payNow(mode):
    print("Paynow fun is called")

def paytm():
    print("Paytm fun is called")

def phonepe():
    print("Phonepe fun is called")

def fampay():
    print("Fampay is called")

app = input("Enter app you want to do payment with:- ")

if app == "phonepe":
    payNow(paytm)
elif app == "fampay":
    payNow(fampay)
elif app == "paytm":
    payNow(paytm)
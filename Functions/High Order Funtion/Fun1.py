def payNow(mode,amt):
    print("Paynow Fun is called")
    mode(amt)

def paytm(amt):
    print("Paytm fun is called")
    print("Amt payed = ",amt)

def phonepay(amt):
    print("Phonepay fun is called")
    print("Amt payed = ",amt)

def fampay(amt):
    print("Fampay fun is called")
    print("Amt payed = ",amt)

app = input("Enter app name:- ")
amount = int(input("Enter amount:- "))

if app == "phonepay":
    payNow(phonepay,amount)
elif app == "fampay":
    payNow(fampay,amount)
elif app == "paytm":
    payNow(paytm,amount)
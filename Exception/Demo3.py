try:
    no1 = int(input("Enter your number:- "))
    no2 = int(input("Enter your number:- "))

    ans = no1 / no2
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
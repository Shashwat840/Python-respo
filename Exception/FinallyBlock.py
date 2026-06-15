try:
    no1 = int(input("Enter a number:- "))
    no2 = int(input("Enter a number:- "))

    ans = no1 / no2
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
finally:
    print("Finally block called")
    print("It is used to end the transction")
    print("It will execute anyhow even if prog have errors")
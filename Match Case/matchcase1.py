choise=int(input("1)For addition \n 2)For Subtraction \n 3)For division\n Enter your choise:- "))

match choise: 
    case 1 : 
        print("Addition Called")
    case 2 :
        print("Subtration Callled")
    case 3:
        print("Divison Called")
    case _ : 
        print("Enter valid choise")

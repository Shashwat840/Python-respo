choise = input("Enter choise :- To continue press y and to discontinue press n")

match (choise):
    case "y"| "Y" | "Yes"|"YES"|"yes" :
        print("Contiuee..")
    case "N"| "n" | "No"|"NO"|"no" :
        print("Discontinue")
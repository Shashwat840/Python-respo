#Multiple inheritance
class Father:
    city = "Dubai"
    Veh = "Harley Davidson"
    def __init__(self):
        self.amt = 200000
        self.a = 200


class Mother:
    city = "China"
    Veh = "hero honda"
    def __init__(self):
        self.b = 100
        self.amt = 100000


class Children(Mother,Father): 
    def __init__(self):
        super().__init__()

    def getInfo(self):
        print("Amt own by mother",self.amt)
        print("Veh own by father",Father.Veh)
        print("Veh own by mother",self.Veh)
        print("City of mother: ",self.city)

c = Children()
c.getInfo()
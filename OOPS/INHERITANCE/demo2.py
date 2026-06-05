class Vechicle:

    def __init__(self,engine,seats,name):
        self.engine = engine
        self.seats = seats
        self.type = name

class Car(Vechicle):
    def __init__(self, engine, seats, name):
        # print("Car constructor is called")
        super().__init__(engine, seats, name) #--> It is used to inherit the properties of parent class

    def getVechileInfo(self):
        print("Engine:= ",self.engine)
        print("Type:= ",self.type)
        print("Seats:= ",self.seats)

c1 = Car("v8",2,"Pagani")
c1.getVechileInfo()
print("===============================")
c2 = Car("v8",2,"Ferrari Vista Spider")
c2.getVechileInfo() 
import datetime
class user:
    def __init__(self,name):
        self.name = name

class Employee(user):
    def __init__(self, name):
        super().__init__(name)
        
    def markAtt(self):
        fopen = open("employee.txt","a")
        fopen.write("employee:- " + self.name + " - " + str(datetime.datetime.now()) + "\n")
        fopen.close()
    

class Manager(user):
    def __init__(self, name):
        super().__init__(name)
    
    def markAtt(self):
        fopen = open("manager.txt","a")
        fopen.write("Manager:- " + self.name + " - " + str(datetime.datetime.now()) + "\n")
        fopen.close()

e = Employee("Ram")
e.markAtt()

m = Manager("Laxman")
m.markAtt()
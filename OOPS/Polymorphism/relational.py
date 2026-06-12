class Employee:
    def __init__(self,sal):
        self.sal = sal
    
    def __eq__(self, value):
        return self.sal == value.sal
    
    def __lt__(self, other):
        return self.sal < other.sal
    
    def __gt__(self, other):
        return self.sal > other.sal
    
    def __le__(self, other):
        return self.sal <= other.sal
    
    def __ge__(self, other):
        return self.sal >= other.sal

e1 = Employee(50000)
e2 = Employee(50000)

if e1 == e2:
    print("Both employees have same salary")
elif e1>e2:
    print(f"e1 have more sal than e2")
else:
    print(f"e2 have more sal than e1")
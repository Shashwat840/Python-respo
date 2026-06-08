from abc import ABC,abstractmethod
class RBI(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def withdraw(self):
        pass

class SBI(RBI):

    def __init__(self):
        super().__init__()
    
    def withdraw(self):
        print("Withdraw done from SBI..")

b = SBI()
b.withdraw()
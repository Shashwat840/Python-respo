#Multi Level inheritance
class Animal:
    def __init__(self):
        print("Animal have no feathers")

class Omivore(Animal):
    def __init__(self):
        super().__init__()
        print("Omivore eat both plants and animals")
class Crow(Omivore):
    def __init__(self):
        super().__init__()
        print("Crow is a Omivore")
c = Crow()
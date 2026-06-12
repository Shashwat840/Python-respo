class Game:
    def __init__(self,score):
        self.score = score

    def __sub__(self, other):
        return other.score - self.score
    
s1 = Game(200) 
s2 =Game(500) 
final = s1 - s2
print(final)
#For div we have __truediv__
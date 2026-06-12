class Cart:
    def __init__(self,items):
        self.items = items

    def __add__(self, other):
        return self.items + other.items

c1 = Cart([{"name":"Iphone","Price":40000}])
c2 = Cart([{"name":"Ipad","Price":30000}])
final = c1 + c2
print(final)